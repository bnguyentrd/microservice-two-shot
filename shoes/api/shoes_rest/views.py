from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from common.json import ModelEncoder
from .models import BinVO, Shoes


class BinVOEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "closet_name",
        "bin_number",
        "bin_size",
        "import_href",
    ]

class ShoeListEncoder(ModelEncoder):
    model = Shoes
    properties = [
        "model_name",
        "manufacturer",
        "color",
        "pictured_url",
        "bin",
        "id",
    ]
    encoders = {
        "bin": BinVOEncoder(),
    }



class ShoeDetailEncoder(ModelEncoder):
    model = Shoes
    properties = [
        "manufacturer",
        "model_name",
        "color",
        "pictured_url",
        "bin",
        "id",
    ]
    encoders = {
        "bin": BinVOEncoder(),
    }


@require_http_methods(["GET", "POST"])
def api_list_shoes(request,bin_vo_id=None):
    if request.method == "GET":
        if bin_vo_id is not None:
            shoes = Shoes.objects.filter(bin=bin_vo_id)
        else:
            shoes = Shoes.objects.all()
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoeListEncoder,
        )
    else:
        content = json.loads(request.body)

        try:
            bin_href=f'/api/bins/{content["bin"]}/'
            bin = BinVO.objects.get(import_href=bin_href)
            content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin"},
                status=400,
            )

        shoes = Shoes.objects.create(**content)
        return JsonResponse(
            shoes,
            encoder=ShoeDetailEncoder,
            safe=False,
        )

@require_http_methods(["GET","DELETE"])
def api_show_shoe(request, pk):
    if request.method == "GET":
        try:
            shoe = Shoes.objects.get(id=pk)
            return JsonResponse(
                shoe,
                encoder=ShoeDetailEncoder,
                safe=False,
            )
        except Shoes.DoesNotExist:
            return JsonResponse (
                {"message": "Shoe doesn't exist"},
                status=400,
            )
    else:
        try:
            count, _=Shoes.objects.filter(id=pk).delete()
            return JsonResponse (
                {"deleted": count > 0}
            )
        except Shoes.DoesNotExist:
            return JsonResponse(
                {"message": "Shoe does not exist"},
                status=400,
            )
