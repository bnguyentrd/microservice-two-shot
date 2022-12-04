from django.db import models


class BinVO(models.Model):
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()
    import_href = models.CharField(max_length=200)

class Shoes(models.Model):
    manufacturer = models.CharField(max_length=250)
    model_name = models.CharField(max_length=250)
    color = models.CharField(max_length=250)
    pictured_url = models.URLField(null=True, blank=True)
    bin = models.ForeignKey (
        BinVO,
        related_name="shoes",
        on_delete=models.PROTECT
    )
