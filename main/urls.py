from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from .views import shipping_view


urlpatterns = [
    path("", views.index, name="index"),
    path('shipping/', shipping_view, name='shipping'),
]