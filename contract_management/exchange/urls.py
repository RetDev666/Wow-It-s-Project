# exchange/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brokerage/create/', views.brokerage_create, name='brokerage_create'),
    path('brokerage/<int:pk>/update/', views.brokerage_update, name='brokerage_update'),
    path('brokerage/<int:pk>/delete/', views.brokerage_delete, name='brokerage_delete'),
]
