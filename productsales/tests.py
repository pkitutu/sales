from django.test import TestCase
from .models import ProductSales
from products.models import Products

# Create your tests here.

class ProductsalesTestCase(TestCase):
	def setUp(self):
		product1 = Products.objects.create(product_name='Shoes', buying_price=10, selling_price=20)
		product2 = Products.objects.create(product_name='Slippers', buying_price=15, selling_price=17)
		ProductSales.objects.create(pk=1,product=product1, units_sold=5, selling_date='2017-01-03')
		ProductSales.objects.create(pk=2,product=product2, units_sold=6, selling_date='2017-01-03')
		ProductSales.objects.create(pk=3,product=product2, units_sold=10, selling_date='2017-01-03')

	def test_product_sales(self):
		sale1 = ProductSales.objects.get(pk=1)
		sale2 = ProductSales.objects.get(pk=2)
		sale3 = ProductSales.objects.get(pk=3)
		self.assertEqual(sale1.units_sold, 5)
		self.assertEqual(sale2.units_sold, 6)
		self.assertEqual(sale3.units_sold, 10)