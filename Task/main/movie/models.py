from django.db import models

# Create your models here.
class TopMovie(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    rating = models.CharField(max_length=10)
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=500)
