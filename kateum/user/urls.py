from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    path('', register, name="register"),
    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('profile/favourites/', views.favourite_list, name='favourite_list'),

]