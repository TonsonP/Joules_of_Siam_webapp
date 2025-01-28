from django.shortcuts import render
from django.http import JsonResponse
from .service_set.dashboard import generated_data, generated_graph_dh_left_graph, generated_graph_dh_right_graph, get_projects_description, get_features_explaination, get_data_electricity_generation_by_sector, get_data_electricitiy_generation_by_type, get_data_electricity_consumption_per_months
from rest_framework.decorators import api_view
from rest_framework.response import Response

def dashboard_home_left_graph(request):
    data = generated_graph_dh_left_graph()
    return JsonResponse(data)

def dashboard_home_right_graph(request):
    data = generated_graph_dh_right_graph()
    return JsonResponse(data)

def dashboard_home(request):
    table_data = generated_data()
    project_description = get_projects_description()
    features_explaination = get_features_explaination()
    context_data = {
        "table_data": table_data, 
        "project_description": project_description,
        "features_explaination": features_explaination
    }

    return render(request, 'dashboard_main/index.html', context_data)

def charts_electricity_generation_graph(request):
    data = get_data_electricitiy_generation_by_type()
    return JsonResponse(data)

def charts_electricity_consumption_graph(request):
    data = get_data_electricity_generation_by_sector()
    return JsonResponse(data)

@api_view(['POST'])
def charts_electricity_consumption_group_by_month(request):

    data = request.data
    sector = data["sector"]

    data = get_data_electricity_consumption_per_months(sector)
    return JsonResponse(data)
    

def charts(request):
    return render(request, 'dashboard_main/charts.html')

def tables(request):
    return render(request, 'dashboard_main/tables.html')
