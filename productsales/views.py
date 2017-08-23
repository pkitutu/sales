from django.shortcuts import render,redirect
from django_datatables_view.base_datatable_view import BaseDatatableView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import  ProductSales
from products.models import Products
from .forms import  ProductsalesForm
from .serializers import ProductsalesSerializer, ProductsSerializer


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

@api_view(['GET'])
def products(request):
	if request.method == 'GET':
		serializer = ProductsSerializer(Products.objects.all(), many=True, read_only=True)
		return Response(serializer.data)

@api_view(['GET'])
def productsales(request):
	if request.method == 'GET':
		serializer = ProductsalesSerializer(ProductSales.objects.all(), many=True, read_only=True)
		return Response(serializer.data)

class ListJson(BaseDatatableView):

	model = ProductSales
	columns = ['product.product_name', 'units_sold', 'selling_date']

	order_columns =  ['product.product_name', 'units_sold', 'selling_date']

	max_display_length = 500