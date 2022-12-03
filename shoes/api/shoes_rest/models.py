from django.db import models
from django.urls import reverse


class BinVO(models.Model):
    closet_name = models.CharField(max_length=150)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()



class Shoes(models.Model):
    manufacturer = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    color = models.CharField(max_length=25)
    picture_url = models.URLField(null=True)
    bin = models.ForeignKey(
        BinVO,
        related_name="shoes",
        on_delete=models.CASCADE,
        null=True
    )


    def get_api_url(self):
        return reverse("api_show_shoe", kwargs={"pk": self.pk})

    def __str__(self):
        return f'This is a {self.color} {self.manufacturer} in {self.bin}'
