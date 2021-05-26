from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.


def home(request):

    # return render(request, 'home/home.html',{"title":"主页"})
    return HttpResponse("WELCOME")


def market(request):
    return render(request, 'market/market.html',{"title":"闪送超市"})


def cart(request):
    return render(request, 'cart/cart.html',{"title":"购物车"})


def mine(request):
    return render(request, 'mine/mine.html',{"title":"我的"})









