from itertools import product
from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product
# Create your views here.
def get_home (request):
    return HttpResponse(f'''<h1> Welcome to the website </h1>
    <h3> We have 3 products go to products page and check them out at your own risk </h3>''')

def get_products (request, product_id):
    product = Product.objects.get(id=product_id)
    return HttpResponse(f''' 
    <p1>
    Product Name: {product.name}. <br>
    Product price: {product.price} KD. <br>
    Discription: {product.description} <br>
    </p1>''')