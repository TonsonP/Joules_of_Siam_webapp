from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
]
