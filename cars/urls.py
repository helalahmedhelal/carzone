from django.urls import path
from . import views
urlpatterns = [
    path('',views.cars,name='cars'),
    path('car_details/<int:id>/',views.car_detail,name='car_details'),
    path('search/',views.search,name='search'),
    
    
]
