from django.urls import path
from . import views

urlpatterns = [
    path('dadd/', views.dadd),
    path('ddetail/', views.ddetail),
    path('ddelete/', views.ddelete),
]