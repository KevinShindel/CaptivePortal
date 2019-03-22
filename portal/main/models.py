from django.db import models


# Create your models here.
class Main(models.Model):
    login = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
