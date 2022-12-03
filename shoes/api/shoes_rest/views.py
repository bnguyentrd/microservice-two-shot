from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import BinVO, Shoes

class BinVODetailEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "id",
        "closet_name",
        "bin_number",
        "bin_size",
    ]

class ShoeListEncoder(ModelEncoder):
    model = Shoes
    properties = ["id"]

    def get_extra_data(self, o):
        return {"bin": o.bin.closet_name}

class ShoeDetailEncoder(ModelEncoder):
    model = Shoes
    properties = [
        "pictured_url",
        "brand",
        "color",
        "bin",
    ]

@require_http_methods(["GET", "POST"])
def api_list_shoes(request):
    if request.method == "GET":
        shoes = Shoes.objects.all()
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoeListEncoder,
        )
    else:
        content = json.loads(request.body)
        shoes = Shoes.objects.create(**content)
        return JsonResponse(
            shoes,
            encoder=ShoeListEncoder,
            safe=False,
        )

@require_http_methods(["GET", "DELETE", "PUT"])
def api_show_shoes(request, pk):
    if request.method == "GET":
        try:
            shoes = Shoes.objects.get(id=pk)
            return JsonResponse(
                shoes,
                encoder=ShoeDetailEncoder
            )
        except Shoes.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            shoes = Shoes.objects.get(id=pk)
            shoes.delete()
            return JsonResponse(
                shoes,
                encoder=ShoeDetailEncoder,
                safe=False,
            )
        except Shoes.DoesNotExist:
            return JsonResponse({"message": "Does not exist"})
    else:
        try:
            content = json.loads(request.body)
            shoes = Shoes.objects.get(id=pk)

            props = ["pictured_url", "brand", "color", "bin"]
            for prop in props:
                if prop in content:
                    setattr(shoes, prop, content[prop])
            shoes.save()
            return JsonResponse(
                shoes,
                encoder=ShoeDetailEncoder,
                safe=False,
            )
        except Shoes.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
