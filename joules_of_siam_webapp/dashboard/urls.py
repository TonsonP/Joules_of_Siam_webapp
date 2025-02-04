from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('_get_dashboard_home_left_graph/', views.dashboard_home_left_graph, name="_get_dashboard_home_left_graph"),
    path('_get_dashboard_home_right_graph/', views.dashboard_home_right_graph, name="_get_dashboard_home_right_graph"),
    path('charts/', views.charts, name='charts'),
    path('_get_charts_electricity_generation_graph/', views.charts_electricity_generation_graph, name="_get_charts_electricity_generation_graph"),
    path('_get_charts_electricity_consumption_graph/', views.charts_electricity_consumption_graph, name="_get_charts_electricity_consumption_graph"),
    path('_post_charts_electricity_consumption_group_by_month_graph', views.charts_electricity_consumption_group_by_month, name="_post_charts_electricity_consumption_group_by_month_graph"),
    path('tables/', views.tables, name='tables'),
    path('predictions/', views.predictions, name='predictions'),
    path('_prediction_electricity_comsumption_forecasting', views.prediction_electricity_comsumption_forecasting, name="_prediction_electricity_comsumption_forecasting")
]
