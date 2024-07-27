from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_home_page(request):
    return render(request, 'temp_homepage/home.html',context={})

def get_about_page(request):
    return render(request, 'temp_homepage/about.html',context={})

def get_contact_page(request):
    return render(request, 'temp_homepage/contact.html',context={})

def get_error_page(request):
    return render(request, 'temp_homepage/404.html',context={})