from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('_get_dashboard_home_left_graph/', views.dashboard_home_left_graph, name="_get_dashboard_home_left_graph"),
    path('_get_dashboard_home_right_graph/', views.dashboard_home_right_graph, name="_get_dashboard_home_right_graph"),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
]
