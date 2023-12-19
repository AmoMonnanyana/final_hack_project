from django.urls import path, include
from django.contrib import admin
from . import views
from .views import order_list, create_order, update_order_status, order_history, return_order, delete_cart, confirm_order
from .views import invoicing, create_invoice, invoice_detail, edit_invoice, delete_invoice, mark_invoice_as_paid, add_to_cart, view_cart, delete_from_cart, increase_cart_quantity, decrease_cart_quantity, order_details



urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('per_product/<int:pk>/', views.per_product, name='per_product'),
    path("product_update/<int:pk>/", views.update, name="product_update"),
    path("delete/<int:pk>/", views.delete, name="product_delete"),
    path("add/", views.add_product, name="product_add"),
    path('marketing/', views.marketing, name='marketing'),
    path('invoicing/', views.invoicing, name='invoicing'),
    path('create_invoice/', create_invoice, name='create_invoice'),
    path('invoice', invoice_detail, name='invoice_detail'),
    path('edit_invoice/<int:pk>/', edit_invoice, name='edit_invoice'),
    path('delete_invoice/<int:pk>/', delete_invoice, name='delete_invoice'),
    path('mark_as_paid/<int:pk>/', mark_invoice_as_paid, name='mark_invoice_as_paid'),
    path('profile/', views.profile, name='profile'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('about/', views.about, name='about'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_list', order_list, name='order_list'),
    path('create order', create_order, name='create_order'),
    path('update_order_status/<int:order_id>/', update_order_status, name='update_order_status'),
    path('order_history', order_history, name='order_history'),
    path('return_order/<int:order_id>/', return_order, name='return_order'),
    # path('registration/', registration, name='registration'),
    path('stock/', views.stock, name='stock'),
    path('add_to_cart/<int:item_id>/', add_to_cart, name="add_to_cart"),
    path('view_cart', view_cart, name='view_cart'),
    path('delete_from_cart/<int:item_id>/', delete_from_cart, name="delete_from_cart"),
    path('increase_cart_quantity/<int:item_id>/', increase_cart_quantity, name="increase_cart_quantity"),
    path('decrease_cart_quantity/<int:item_id>/', decrease_cart_quantity, name="decrease_cart_quantity"),
    path('order_details', order_details, name='order_details'),
    path('delete_cart', delete_cart, name='delete_cart'),
    path('confirm_order/<int:pk>/', confirm_order, name='confirm_order'),
]
