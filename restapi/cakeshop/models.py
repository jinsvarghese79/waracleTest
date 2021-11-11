from django.db import models


# Create your models here.
class Cake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)
    yumFactor = models.IntegerField(max_length=1)

