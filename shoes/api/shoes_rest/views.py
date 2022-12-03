from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Shoes, BinVO
from common.json import ModelEncoder
import json



class BinVODetailEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "import_href",
        "closet_name",
        "bin_number",
        "bin_size",
    ]


class ShoesListEncoder(ModelEncoder):
    model = Shoes
    properties = [
        "id",
        "model_name",
        "color",
        "manufacturer",
        "pictured_url",
        "bin",
    ]

    encoders={
        "bin": BinVODetailEncoder()
    }


class ShoesDetailEncoder(ModelEncoder):
    model = Shoes
    properties = [
        "manufacturer",
        "model_name",
        "color",
        "pictured_url",
        "bin",
    ]
    encoders = {
        "bin": BinVODetailEncoder()
        }


@require_http_methods(["GET", "POST"])
def api_list_shoes(request, bin_vo_id=None):
    if request.method == "GET":
        if bin_vo_id is not None:
            shoes = Shoes.objects.filter(bin=bin_vo_id)
        else:
            shoes = Shoes.objects.all()
        return JsonResponse({"shoes": shoes}, encoder=ShoesListEncoder)
    else:
        content = json.loads(request.body)
        try:
            bin_href = content["bin"]
            bin = BinVO.objects.get(import_href=bin_href)
            content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin id"},
                status=400,
            )

        shoes = Shoes.objects.create(**content)
        return JsonResponse(
            shoes,
            encoder=ShoesDetailEncoder,
            safe=False,
        )

@require_http_methods(["DELETE", "GET", "PUT"])
def api_show_shoes(request, pk):
    if request.method == "GET":
        try:
            shoes = Shoes.objects.get(id=pk)
            return JsonResponse(
                shoes,
                encoder=ShoesDetailEncoder,
                safe=False
            )
        except Shoes.DoesNotExist:
            return JsonResponse({"message": "Invalid shoes ID"}, status=400)
    elif request.method == "DELETE":
        try:
            count, _ = Shoes.objects.filter(id=pk).delete()
            return JsonResponse({"deleted": count > 0})
        except Shoes.DoesNotExist:
            return JsonResponse({"message": "Invalid shoes ID"}, status=400)
    else: # PUT
        try:
            content = json.loads(request.body)
            Shoes.objects.filter(id=pk).update(**content)
            shoes = Shoes.objects.get(id=pk)
            return JsonResponse(
                shoes,
                encoder=ShoesDetailEncoder,
                safe=False
            )
        except Shoes.DoesNotExist:
            return JsonResponse({"message": "Invalid shoes ID"}, status=400)
