from django.urls import path
from . import views

urlpatterns = [

path('',views.pqr_list,name='pqr_list'),

path('create/',views.pqr_create,name='pqr_create'),

path('<int:id>/',views.pqr_detail,name='pqr_detail'),

path('<int:id>/delete/',views.pqr_delete,name='pqr_delete'),

]