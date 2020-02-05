from django.urls import path
from . import views

urlpatterns = [
    path('badd/', views.badd),
    path('bdetail/', views.bdetail),
    
]