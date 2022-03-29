from django.db import models

# Create your models here.
class Tech(models.Model):
    name = models.CharField(max_length=500)
    processor = models.CharField(max_length=250)
    display = models.CharField(max_length=500)
    ram = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.CharField(default=None, blank=True, null=True, max_length=2000)
        
