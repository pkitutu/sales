from __future__ import unicode_literals

from django.db import models
from products.models import Products

# Create your models here.
#Products model
class ProductSales(models.Model):
	product = models.ForeignKey(Products, on_delete=models.CASCADE)
	units_sold = models.IntegerField()
	selling_date = models.DateField()