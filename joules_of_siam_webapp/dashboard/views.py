from django.shortcuts import render
from django.http import JsonResponse
from .service_set.dashboard import generated_data, generated_graph_dh_left_graph


def dashboard_home_left_graph(request):
    data = generated_graph_dh_left_graph()
    return JsonResponse(data)

def dashboard_home(request):
    table_data = generated_data()
    return render(request, 'dashboard_main/index.html', {"table_data": table_data})

def charts(request):
    return render(request, 'dashboard_main/charts.html')

def tables(request):
    return render(request, 'dashboard_main/tables.html')
