from django.contrib import admin
from .models import Shoes, BinVO

admin.site.register(Shoes)
admin.site.register(BinVO)

# @admin.site.register(Shoes)
# class ShoesAdmin(admin.ModelAdmin):
#     pass

# @admin.site.register(BinVO)
# class BinVOAdmin(admin.ModelAdmin):
#     pass
