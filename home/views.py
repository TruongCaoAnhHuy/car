from django.http import HttpResponse
from django.shortcuts import render
from .form import LoginForm, RegisterForm, form_contact
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
class get_home(View):
    def get(self, request):
        cF = form_contact
        return render(request, 'home/home.html', {'cF':cF})
    def post(self, request):
        if request.method == "POST":
            cF = form_contact(request.POST)
        if cF.is_valid():
            cF.save()
            return HttpResponse("Save success!")
        else:
            return HttpResponse("not Post")

def get_vehicles(request):
    return render (request, 'home/vehicles.html')

def get_services(request):
    return render (request, 'home/services.html')

def get_featured(request):
    return render (request, 'home/featured.html')

def get_reviews(request):
    return render (request, 'home/reviews.html')

def get_car_selling(request):
    return render (request, 'home/car_selling.html')

def get_parts_repair(request):
    return render (request, 'home/repair.html')

def get_car_insurance(request):
    return render (request, 'home/car_insurance.html')

def get_battery(request):
    return render (request, 'home/battery.html')

def get_oil(request):
    return render (request, 'home/oil_change.html')

def get_support(request):
    return render (request, 'home/support.html')

class get_login(View):
    def get(self, request):
        lG = LoginForm
        return render(request, 'home/login.html', {'lG': lG})
    def post(self, request):
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None: 
            login(request, user)
            return render(request, 'home/home1.html')
        else:
            messages.error(request, 'Đăng nhập không thành công. Vui lòng kiểm tra tên người dùng và mật khẩu.')
            return render(request, 'home/home.html')
    
class get_register(View):
    def get(self, request):
        rG = RegisterForm
        return render(request, 'home/register.html', {'rG': rG})
    def post(seft, request):
        username = request.POST['user_name']
        password = request.POST['password']
        c_password = request.POST['c_password']
        email = request.POST['email']
        if password == c_password:
            user = User.objects.create_user(username, email, password)
            user.save()
            return render (request , 'home/login.html')

        else:
            return HttpResponse('home/login.html')

class get_contact(View):
    def get(self, request):
        cF = form_contact
        return render(request, 'home/contact.html', {'cF':cF})
    def post(self, request):
        if request.method == "POST":
            cF = form_contact(request.POST)
        if cF.is_valid():
            cF.save()
            return HttpResponse("Save success!")
        else:
            return HttpResponse("not Post")
        
class get_contactForm(View):
    def post(self, request):
        if request.method == "POST":
            cF = form_contact(request.POST)
        if cF.is_valid():
            cF.save()
            return HttpResponse("Save success!")
        else:
            return HttpResponse("not Post")
