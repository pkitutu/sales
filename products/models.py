from __future__ import unicode_literals

from django.db import models

# Create your models here.
#Products model
class Products(models.Model):
	product_name = models.CharField(max_length=64)
	buying_price = models.CharField(max_length=128)
	selling_price = models.CharField(max_length=64, null=True)