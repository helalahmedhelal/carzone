from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.

def home(request):
    team_member=Team.objects.all()
    fetured_cars=Car.objects.filter(is_featured=True).order_by('-created_date')
    models=Car.objects.values('model').distinct()
    data={
        'team_member':team_member,
        'fetured_cars':fetured_cars,
        'models':models
    }
    return render(request,'pages/home.html',data)

def contact(request):
    return render(request,'pages/contact.html')

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)
    
def services(request):
    return render(request,'pages/services.html')    