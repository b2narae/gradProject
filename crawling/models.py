from django.db import models
from django.utils import timezone

class Car(models.Model):
    Model = models.CharField(max_length=30)
    Maker = models.CharField(max_length=10)
    Year = models.IntegerField()

    Size = models.CharField(max_length=10)
    Fuel = models.CharField(max_length=10)
    Accident = models.CharField(max_length=10)

    Shift = models.CharField(max_length=10)
    Color = models.CharField(max_length=10)
    Distance = models.IntegerField()

    Price = models.IntegerField()

    def __str__(self):
        return self.Model

    def __price__(self):
        return self.Price

# Create your models here.
