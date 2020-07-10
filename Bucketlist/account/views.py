from django.shortcuts import render

# Create your views here.


def register_page(request):
    return render(request, 'signup.html')


def login_page(request):
    return render(request, 'login.html')
