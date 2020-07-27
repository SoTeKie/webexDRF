from django.db import models


class Podnet(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image = models.ImageField()
    uploadDate = models.DateTimeField(auto_now_add=True)
