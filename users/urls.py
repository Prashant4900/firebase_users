from django.urls import path
from . import views

urlpatterns = [
    path('users/firebaseusers/', views.index),
    path('', views.index),
]
