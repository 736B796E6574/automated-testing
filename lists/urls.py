from django.contrib import admin
from django.urls import path, include
from lists.views import home_page

urlpatterns = [
    path('', home_page, name='allposts'),
]