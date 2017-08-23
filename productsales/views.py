from django.shortcuts import render,redirect
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import  ProductSales
from .forms import  ProductsalesForm

# Create your views here.

def create(request):
	if request.method == 'POST':
		form = ProductsalesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('productsales:list')
	else:
		form =  ProductsalesForm()
	context = {'form': form}
	return render(request, 'productsales/create.html', context)

def list(request):
	return render(request, 'productsales/list.html')

class ListJson(BaseDatatableView):

	model = ProductSales
	columns = ['product.product_name', 'units_sold', 'selling_date']

	order_columns =  ['product.product_name', 'units_sold', 'selling_date']

	max_display_length = 500