from django.shortcuts import render
from django.http import JsonResponse
from .service_set.dashboard import generated_data, generated_graph_dh_left_graph, generated_graph_dh_right_graph, get_projects_description, get_features_explaination, get_data_electricity_generation_by_sector


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

def charts_top_graph(request):
    data = get_data_electricity_generation_by_sector()
    return JsonResponse(data)

def charts(request):
    return render(request, 'dashboard_main/charts.html')

def tables(request):
    return render(request, 'dashboard_main/tables.html')
