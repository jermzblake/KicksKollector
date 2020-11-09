from django.db import models

# Create your models here.
class Kick(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    releasedate = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
