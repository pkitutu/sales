from rest_framework import serializers

from products.models import Products
from productsales.models import ProductSales


class ProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		fields = ('product_name','buying_price','selling_price',)


class ProductsalesSerializer(serializers.ModelSerializer):
	product = ProductsSerializer(read_only=True)

	class Meta:
		model = ProductSales
		fields = ('product','units_sold','selling_date',)