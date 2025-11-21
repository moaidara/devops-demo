from queue import PriorityQueue
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'dashbord.html', {'products' : products})


@csrf_exempt
def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")

        Product.objects.create(
            name=name,
            price=price
        )

        return redirect("home")

    return redirect("home")

@csrf_exempt
def update_product(request):
    if request.method == "POST":
        product_id = request.POST.get('id')
        product_name = request.POST.get('name')
        product_price = request.POST.get('price')

        print(product_id)
        print(product_name)
        print(product_price)
        product = get_object_or_404(Product, id = product_id)

        product.name = product_name
        product.price = product_price
        product.save()

        print(product.name)
        print(product.price)

        return redirect('home')
    return redirect('home')
    
@csrf_exempt
def delete_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('id')

        product = get_object_or_404(Product, id=product_id)
        product.delete()

        return redirect('home')
    return redirect('home')