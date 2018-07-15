from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Coordinate(models.Model):
    latitude = models.TextField(max_length=100)
    longitude = models.TextField(max_length=100)
