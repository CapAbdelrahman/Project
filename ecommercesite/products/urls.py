from django.urls import path,include
from. import views



urlpatterns = [
   path('',views.home,name="hm"),
   path('product/<int:productid>',views.product,name="pr"),
   path('Samsung',views.samsung,name="samsung"),
   path('Huawei',views.huawei,name="hwawei"),
   path('Apple',views.Apple,name="Apple"),
   path('cart',views.cart,name="category"),
]