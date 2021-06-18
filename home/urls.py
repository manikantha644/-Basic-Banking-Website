from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name='home'),
    path("transaction", views.transaction, name='transaction'),
    path('customers', views.customers, name='customers'),
    path("<int:customer_id>",views.customerid,name="customerid"),
    path("view", views.view, name='view'),
    path("search",views.search,name='search'),
]