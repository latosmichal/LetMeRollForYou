from django.urls import path
from . import views

urlpatterns = [
    path('', views.roll_main, name='roll_main'),
]