# from itertools import product
# from multiprocessing import context
from django.shortcuts import render

# from django.http import HttpResponse

from products.models import Product

# Create your views here.
def get_home(request):
    return render(request, "home.html")

    # return HttpResponse(f'''<h1> Welcome to the website </h1>
    # <h3> We have 3 products go to products page and check them out </h3>''')


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    #  Convert object to dictionary
    context = {
        "product": {
            "name": product.name,
            "price": product.price,
            "description": product.description,
        }
    }
    return render(request, "product-detail.html", context)
    # return HttpResponse(
    #     f"""
    # <p1>
    # Product Name: {product.name}. <br>
    # Product price: {product.price} KD. <br>
    # Discription: {product.description} <br>
    # </p1>"""
    # )


def get_products(request):
    products = Product.objects.all()
    new_product = []
    for product in products:
        new_product.append(
            {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "description": product.description,
            }
        )
    context = {"products": new_product}
    return render(request, "product-list.html", context)
