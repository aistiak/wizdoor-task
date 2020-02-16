from django.shortcuts import render
from django.http import HttpResponse,JsonResponse 
from django.core import serializers
from api.models import *
from api.serializers import *
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt    
def index(request):
    users = User.objects.all()
    res = UserSerializer(users,many=True)
    return JsonResponse(res.data,safe=False)


# @csrf_exempt
# def order_list(request):
#     if request.method == 'GET':
#         products = Order.objects.all()
#         response = OrderSerializer(products,many=True)
#         return JsonResponse(response.data,safe=False) 
#         # pass  
@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        response = ProductSerializer(products,many=True)
        return JsonResponse(response.data,safe=False) 
        # pass  

@csrf_exempt
def category_product(request):
    if request.method == 'GET':
        products = Category.objects.all()
        response = CategoryWithProductCountSerializer(products,many=True)
        return JsonResponse(response.data,safe=False) 
        # pass  


@csrf_exempt
def customers(request):
    if request.method == 'GET':
        location = request.GET.get('location')
        if location :
            customers = Customer.objects.filter(location__contains=location)
        else:
            customers = Customer.objects.all()    
            
        response  = CustomerOrderDetail(customers,many=True)
        return JsonResponse(response.data,safe=False)
        # return HttpResponse(response.data)