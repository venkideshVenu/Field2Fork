from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_page, name="homepage"),
    path('about/', views.get_about_page, name="aboutpage"),
    path('contact/', views.get_contact_page, name="contactpage"),
    path('pagenotfound/', views.get_error_page, name="notfound"),
]
