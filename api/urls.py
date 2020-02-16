from django.urls import path
from . import views 


urlpatterns = [
    # path('',views.index,name='index'),
    path('products',views.product_list,name='product_list'),
    path('category/count',views.category_product,name='category_product'),
    path('customers',views.customers,name='customers'),
]
