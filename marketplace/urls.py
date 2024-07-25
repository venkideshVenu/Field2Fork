from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.market_place, name="market"),
     path('<slug:category_slug>/', views.store, name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail, name='product_detail'),
]
