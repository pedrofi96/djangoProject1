from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120) #max length = required
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    summary = models.TextField()
