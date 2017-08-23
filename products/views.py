from django.shortcuts import render,redirect
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import Products
from .forms import ProductsForm

# Create your views here.

def create(request):
	if request.method == 'POST':
		form = ProductsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('products:list')
	else:
		form = ProductsForm()
	context = {'form': form}
	return render(request, 'products/create.html', context)

def list(request):
	return render(request, 'products/list.html')

class ListJson(BaseDatatableView):

	model = Products
	columns = ['product_name', 'buying_price', 'selling_price']

	order_columns =  ['product_name', 'buying_price', 'selling_price']

	max_display_length = 500