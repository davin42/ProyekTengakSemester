from django.db import models

# Create your models here.

class Ruangan(models.Model):
    nomor = models.IntegerField()
    ketersediaan = models.CharField(max_length=255)