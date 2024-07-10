from django.db import models

class Records(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone_number=models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    createdAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name