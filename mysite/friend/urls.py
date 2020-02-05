from django.urls import path
from . import views

urlpatterns = [
    path('fadd/', views.fadd),
    path('fdetail/', views.fdetail),
    path('fdelete/', views.fdelete),
]