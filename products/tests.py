from django.test import TestCase
from .models import Products

# Create your tests here.

class ProductsalesTestCase(TestCase):
	def setUp(self):
		Products.objects.create(product_name='Shoesk', buying_price=10, selling_price=20)
		Products.objects.create(product_name='Slippersk', buying_price=15, selling_price=17)
		

	def test_products(self):
		product1 = Products.objects.get(product_name='Shoesk')
		product2 = Products.objects.get(product_name='Slippersk')
		self.assertEqual(product1.buying_price, 10)
		self.assertEqual(product1.selling_price, 20)
		self.assertEqual(product2.buying_price, 15)
		self.assertEqual(product2.selling_price, 17)

