from django.shortcuts import render

# Since this projects is small, I decide to keep everything in one place
def generated_data():
    pass

def dashboard_home(request):
    return render(request, 'dashboard_main/index.html')

def charts(request):
    return render(request, 'dashboard_main/charts.html')

def tables(request):
    return render(request, 'dashboard_main/tables.html')
