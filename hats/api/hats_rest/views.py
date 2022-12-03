from django.shortcuts import render
from common.json import ModelEncoder
from .models import LocationVO, Hats
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

import json

class LocationVODetailEncoder(ModelEncoder):
    model = LocationVO
    properties = [
        "closet_name",
        "section_number",
        "shelf_number",
        "import_href"
        ]

class HatListEncoder(ModelEncoder):
    model = Hats
    properties = [
        "fabric",
        "style_name",
        "color",
        "picture_url",
        "id"
    ]
    def get_extra_data(self, o):
        return {"location": o.location.closet_name}



class HatDetailEncoder(ModelEncoder):
    model = Hats
    properties = [
        "fabric",
        "style_name",
        "color",
        "picture_url",
        "id",
    ]
    encoders = {
        "location": LocationVODetailEncoder(),
    }

@require_http_methods(["DELETE", "GET"])
def api_show_hat(request, pk):
    if request.method == "GET":
            hat = Hats.objects.get(id=pk)
            return JsonResponse(
                hat,
                encoder=HatDetailEncoder,
                safe=False
            )
    else:
        request.method == "DELETE"
        count, _ = Hats.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})



@require_http_methods(["GET", "POST"])
def api_list_hats(request):
    if request.method == "GET": #listing out the hats
        hats = Hats.objects.all()
        return JsonResponse(
            {"hats": hats},
            encoder = HatListEncoder,
        )
    else: #creating a hat
        content = json.loads(request.body)

        try:
            location_href = content["location"]
            location = LocationVO.objects.get(import_href=location_href)
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location id"},
                status=400,
            )
        hat = Hats.objects.create(**content)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )