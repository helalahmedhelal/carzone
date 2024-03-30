from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def cars(request):
    cars=Car.objects.all()
    items_per_page =2
    paginator = Paginator(cars, items_per_page)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)
    
    data={
        'cars':pages
    }
    return render(request,'car_pages/cars.html',data)

def car_detail(request,id):
    
    car_detail=get_object_or_404(Car, pk=id)
    data={
        'car_detail':car_detail
    }
    return render(request,'car_pages/car_details.html',data)

def search(request): 
    keyword = request.GET.get('keyword')
    search_results = Car.objects.all()
    if keyword:
        # Filter the queryset based on the keyword
        search_results = search_results.filter(Q(description__icontains=keyword) | Q(car_title__icontains=keyword))
        
    if 'model' in request.GET:
        model=request.GET['model']
        if model:
           search_results=Car.objects.filter(model__iexact=model)  
    
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
           search_results=Car.objects.filter(Q(price__gte=min_price) , Q(price__lte=max_price))          
    data={
         'search_results':search_results,
         
         
        }
    return render(request,'pages/search.html',data)