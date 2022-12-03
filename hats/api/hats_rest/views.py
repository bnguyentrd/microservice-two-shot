from django.shortcuts import render
from common.json import ModelEncoder
from .models import LocationVO, Hat
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json


# Create your views here.
class LocationVODetailEncoder(ModelEncoder):
    model = LocationVO
    properties = [
        "id",
        "closet_name",
        "shelf_number",
        "section_number",
        "import_href",
    ]


class HatListEncoder(ModelEncoder):
    model = Hat
    properties = ["id"]

    def get_extra_data(self, o):
        return {"location": o.location.closet_name}


class HatDetailEncoder(ModelEncoder):
    model = Hat 
    properties = [
        "id",
        "fabric",
        "style_name",
        "color",
        "picture_url",
        "location",
    ]


@require_http_methods(["GET", "POST"])
def api_list_hats(request):
    if request.method == "GET":
        hats = Hat.objects.all()
        return JsonResponse(
            {"hats": hats},
            encoder=HatListEncoder,
        )
    else:
        content = json.loads(request.body)
        hats = Hat.objects.create(**content)
        return JsonResponse(
            hats,
            encoder=HatDetailEncoder,
            safe=False,
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def api_show_hat(request, pk):
    if request.method == "GET":
        try:
            hat = Hat.objects.get(id=pk)
            return JsonResponse(
                hat,
                encoder=HatDetailEncoder,
                safe=False,
            )
        except Hat.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response 
    elif request.method == "DELETE":
        try:
            hats = Hat.objects.get(id=pk)
            hats.delete()
            return JsonResponse(
                hats,
                encoder=HatDetailEncoder,
                safe=False,
            )
        except Hat.DoesNotExist:
            return JsonResponse({"message": "Does not exist"})
    else:
        content = json.loads(request.body)
        try:
            if "location" in content:
                location = LocationVO.objects.get(closet_name=content["location"])
                content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid state abbreviation"},
                status=400,
            )
        Hat.objects.filter(id=pk).update(**content)
        hat = Hat.objects.get(id=pk)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )

