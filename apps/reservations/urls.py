# apps/reservations/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('create/', views.reservation_create, name='reservation_create'),
    path('<int:id>/', views.reservation_detail, name='reservation_detail'),
    path('<int:id>/delete/', views.reservation_delete, name='reservation_delete'),
]