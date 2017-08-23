from django import forms

from .models import Products


class ProductsForm(forms.ModelForm):
	class Meta:
		model = Products
		fields = ('product_name', 'buying_price', 'selling_price')
	def clean(self):
		cleaned_data = self.cleaned_data
		buying_price = self.cleaned_data.get('buying_price')
		selling_price = self.cleaned_data.get('selling_price')
		if (selling_price)<buying_price:
			self.add_error('selling_price', 'Selling Price should be higher than buying price')
