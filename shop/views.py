from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm
from .recommender import Recommender
def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    products=Product.objects.all()
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)
    return render(request,'shop/list.html',{'category':category,'categories':categories,'products':products})

def product_detail(request,id,slug):
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    r=Recommender()
    recommeded_products=r.suggest_products_for([product], 2)
    return render(request,'shop/detail.html',{'product':product,'cart_product_form': cart_product_form,'recommeded_products':recommeded_products})