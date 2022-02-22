from django.db import models
from random import randint

# Create your models here.


def random_token():
    return randint(100000, 999999)


class Category(models.Model):
    category_name = models.CharField(max_length=300)
    category_price = models.IntegerField()

    def __str__(self):
        return self.category_name


class Vehicle(models.Model):
    vehicle_owner = models.CharField(max_length=300)
    vehicle_name = models.CharField(max_length=200)
    vehicle_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    vehicle_number = models.CharField(max_length=200)
    vehicle_color = models.CharField(max_length=200)
    vehicle_image = models.ImageField(upload_to="images/vehicle/")
    owner_image = models.ImageField(upload_to="images/owner/")
    vehicle_token = models.IntegerField(default=random_token)
    vehicle_arrival = models.DateTimeField(auto_now_add=True)
    vehicle_departure = models.DateTimeField(auto_now_add=False,blank=True,null=True)

    def __str__(self):
        return self.vehicle_owner