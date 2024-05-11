from django.db import models

class Parametr(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    parametrs = models.ManyToManyField('Parametr', blank=True)
