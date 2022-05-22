from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.

@require_POST
def cart_add(request,productid):
	cart = Cart(request)
	product = get_object_or_404(Product,id=productid)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(
			product=product,
			quantity=cd['quantity'],
			update_quantity=cd['update']
			)
	return redirect('cart:cart_detail')

def cart_remove(request,productid):
	cart = Cart(request)
	product = get_object_or_404(Product,id=productid)
	cart.remove(product)
	return redirect('cart:cart_detail')

def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity':item['quantity'],'update':True})
	context = {
		'cart':cart
	}
	return render(request,'cart/detail.html',context)


def home (request):
    return render (request,'pages/homepage.html',{
        'all': Product.objects.order_by('-id'),

    })