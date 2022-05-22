from unicodedata import category
from django.shortcuts import render
from .models import Product
from .models import Category
from .models import cart
from cart.forms import CartAddProductForm
# Create your views here.
def home (request):
    return render (request,'pages/homepage.html',{
        'all': Product.objects.order_by('-id'),

    })

def cart (request):
    cart1= Product.objects.all()
    Cart=cart()
    Cart.name= cart1.name
    Cart.image= cart1.image
    Cart.description= cart1.description
    Cart.price= cart1.price
    Cart.save()
    rows=Product.objects.all()
    cart_item=cart.objects.all()
    categories=Category.objects.all()
    return render (request,'pages/cart.html',{'rows':rows})
   



    
def samsung (request):
    return render (request,'pages/Samsung.html',{
        'sam' : Product.objects.filter(category_id=1)
    })

def huawei (request):
    return render (request,'pages/Huawei.html',{
        'hwe' : Product.objects.filter(category_id=2)
        
    })

def Apple (request):
    return render (request,'pages/Apple.html',{
        'app' : Product.objects.filter(category_id=3)
    })

def product (request, productid):
    product= Product.objects.get(id=productid)
    cart_product_form = CartAddProductForm()
    return render (request,'pages/product.html',{'product':product,
    'cart_product_form':cart_product_form})