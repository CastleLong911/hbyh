from django.db import models

# Create your models here.

class Module(models.Model):
    moduleName = models.CharField(max_length=20)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    on = models.CharField(max_length=3, default="off")