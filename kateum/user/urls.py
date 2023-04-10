from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    path('', register, name="register"),
 ]