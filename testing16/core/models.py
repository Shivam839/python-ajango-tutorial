from django.db import models

# Create your models here.

class Recipes(models.Model):
    name=models.CharField(max_length=100)
    instruction=models.TextField(max_length=1000)
    imageAdress=models.CharField(max_length=500)

    def __str__(self):
        return self.name