from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    roll = models.IntegerField()
    program = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
