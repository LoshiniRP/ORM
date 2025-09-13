from django.db import models
from django.contrib import admin
class Car_DB(models.Model):
    car_Brand=models.CharField(max_length=10)
    color=models.CharField(max_length=10)
    safety_Features=models.CharField(max_length=50)
    car_ID=models.IntegerField(primary_key=True)
    car_Price=models.IntegerField()
class Car_DBAdmin(admin.ModelAdmin):
    list_display=["car_Brand","color","safety_Features","car_ID","car_Price"]