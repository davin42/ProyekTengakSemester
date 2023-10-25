from django.db import models

# Create your models here.

class Ruangan(models.Model):
    nomor = models.IntegerField()
    ketersidiaan = models.CharField(max_length=255)