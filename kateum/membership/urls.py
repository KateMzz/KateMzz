from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    path('membership/', membership, name="membership"),
    path('cards/', cards, name="cards"),
    path('checkout/', checkout, name="checkout"),
    path('payment_successful', views.payment_successful, name='payment_successful'),
    path('payment_cancelled', views.payment_cancelled, name="payment_cancelled"),
    path('stripe_webhook', views.stripe_webhook, name="stripe_webhook")
 ]