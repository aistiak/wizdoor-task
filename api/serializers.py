# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model   = User
        fields  = ['email']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Product  
        fields  = ['id','name']


class CategoryWithProductCountSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category 
        fields = ['id','title','product_count']

    def get_product_count(self,obj):
        return obj.product_set.count()                   

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id','products']

class CustomerOrderDetail(serializers.ModelSerializer):
    user = UserSerializer()
    orders = serializers.SerializerMethodField()
    class Meta:
        model  = Customer 
        fields = ['name','location','user','orders']

    def get_orders(self,obj):
        odder_querset = obj.order_set.all()
        return OrderSerializer(odder_querset,many=True).data

