from __future__ import unicode_literals

from django.db import models

# Create your models here.
#Products model
class Products(models.Model):
	product_name = models.CharField(max_length=64)
	buying_price = models.IntegerField()
	selling_price = models.IntegerField()

	def __str__(self): #return category as default
		return self.product_name