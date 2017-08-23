from django.test import TestCase
from .models import Products

# Create your tests here.

class ProductTestCase(TestCase):
	def setUp(self):
		Products.objects.create(product_name='Shoes', buying_price=10, selling_price=20)
		Products.objects.create(product_name='Slippers', buying_price=15, selling_price=17)
		

	def test_products(self):
		product1 = Products.objects.get(product_name='Shoes')
		product2 = Products.objects.get(product_name='Slippers')
		self.assertEqual(product1.buying_price, 10)
		self.assertEqual(product1.selling_price, 20)
		self.assertEqual(product2.buying_price, 15)
		self.assertEqual(product2.selling_price, 17)

