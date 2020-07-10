from django.shortcuts import render, redirect
from .models import wishes
from django.utils import timezone
from .forms import wishform, myuserform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def homepage(request):

    wishlist = wishes.objects.all()
    context = {"wishlist": wishlist}

    return render(request, 'home.html', context=context)


def makewish(request):
    form = wishform()

    if request.method == 'POST':

        form = wishform(request.POST)

        if form.is_valid():
            print(request.user)
            blist = form.save(commit=False)
            blist.author = request.user
            form.save()
            return redirect('/')

    wishlist = wishes.objects.all()
    context = {"wishlist": wishlist, "form": form}
    return render(request, 'main.html', context=context)


def makeuser(request):
    form = myuserform()

    if request.method == 'POST':
        form = myuserform(request.POST)
        if form.is_valid():
            form.save()

    all_user = User.objects.all()
    context = {"all_user": all_user, "form": form}
    return render(request, 'login.html', context=context)


def login_user(request):

    if request.method == 'POST':
        user = request.POST.get('user_login')
        password = request.POST.get('pass_login')

        id = authenticate(request, username=user, password=password)
        if id is not None:
            login(request, id)
            return redirect('makewish')
        else:
            print('wrong')

    context = {}
    return render(request, 'signin.html', context=context)
