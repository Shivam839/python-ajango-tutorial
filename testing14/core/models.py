from django.db import models

# Create your models here.

class ProjectComplete(models.Model):
    name= models.CharField(max_length=50)
    emailId= models.EmailField(max_length=50)
    phoneNumber = models.CharField(max_length=20)
    totalProject = models.IntegerField()
    address = models.CharField(max_length=200)
    rollNumber = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name

