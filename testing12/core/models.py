from django.db import models

# Create your models here.

class students(models.Model):
    name=models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    section = models.PositiveIntegerField()
    emailId=models.EmailField(max_length=100,null=True, blank=True)
    
    def __str__(self):
        return self.name
