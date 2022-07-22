from django.contrib import admin
from django.urls import path
from .views import product_detail_view, product_create_view, render_initial_data, dynamic_lookup_view, product_list_view

app_name='products'
urlpatterns = [
    path('', product_list_view, name="products-list"),
    path('product/<int:id>/', dynamic_lookup_view, name='product'),
    path('initial/', render_initial_data, name='initial'),
    path('create/', product_create_view, name='create'),
    #path('product/', product_detail_view, name='product'),
]