from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_blog,name='addblog'),
    path('save/',views.save_blog,name='save'),
    path('<int:article_id>/',views.article_view,name='getarticle'),
]
