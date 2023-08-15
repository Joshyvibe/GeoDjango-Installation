from django.db import models
from django.contrib.gis.db import models as gismodels



class Location(models.Model):
    country = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    point = gismodels.PointField(blank=True, null=True, srid=4326)


    def __str__(self):
        return self.country
