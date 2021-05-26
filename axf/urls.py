
from django.urls import path
# from django.conf.urls import url
from axf import views

urlpatterns = [
    path(r'home/', views.home, name="home"),
    path(r'market/', views.market, name="market"),
    path(r'cart/', views.cart, name="cart"),
    path(r'mine/', views.mine, name="mine"),
]