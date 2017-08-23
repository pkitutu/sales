from datetime import *
from django import forms

from .models import ProductSales


class ProductsalesForm(forms.ModelForm):
	class Meta:
		model = ProductSales
		fields = ('product', 'units_sold', 'selling_date')

	def clean(self):
		cleaned_data = self.cleaned_data
		selling_date = self.cleaned_data.get('selling_date')
		if selling_date != None and str(selling_date) > str(date.today()):
			self.add_error('selling_date', "Selling date can not be in the future")