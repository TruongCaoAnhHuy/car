from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.get_home.as_view(), name='home'),
    path('vehicles/', views.get_vehicles, name='vehicles'),
    path('services/', views.get_services, name='services'),
    path('featured/', views.get_featured, name='featured'),
    path('reviews/', views.get_reviews, name='reviews'),
    path('contact/', views.get_contact.as_view(), name='contact'),
    path('contactform/', views.get_contactForm.as_view(), name='contactform'),
    path('login/', views.get_login.as_view(), name='login'),
    path('register/', views.get_register.as_view(), name='register'),
    path('carselling/', views.get_car_selling, name='carselling'),
    path('repair/', views.get_parts_repair, name='repair'),
    path('insurance/', views.get_car_insurance, name='insurance'),
    path('battery/', views.get_battery, name='battery'),
    path('oilchange/', views.get_oil, name='oilchange'),
    path('support/', views.get_support, name='support'),
]   