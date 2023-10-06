from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm

def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    products=Product.objects.filter(available=True)

    if category_slug:
        category=get_object_or_404(Category, slug=category_slug)
        products=products.filter(category=category)
    return render(request,'shop/list.html',{'categories':categories,
                                            'category':category,
                                            'products':products,})
def product_detail(request, id, slug):
    product=get_object_or_404(Product, id=id, slug=slug, available=True)
    related_products=Product.objects.filter(category=product.category).exclude(id=id)[:3]
    cart_product_form=CartAddProductForm()
    return render(request, 'shop/detail.html',{'product':product,'related_products':related_products,'cart_product_form':cart_product_form})

