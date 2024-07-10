from django.db import models

# Create your models here.

class Pricing(models.Model):
    type=models.CharField(max_length=30)
    pricePerMonth=models.PositiveIntegerField()
    numberOfUsers = models.PositiveIntegerField()
    storageInGB = models.PositiveIntegerField()
    support = models.CharField(max_length=100)
    helpCenterAccess = models.BooleanField()

    def __str__(self):
        return self.type

class Students(models.Model):
    name=models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=10)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
