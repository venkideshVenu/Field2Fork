from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_home_page(request):
    return render(request, 'temp_homepage/homepage.html',context={})