from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
def index(request):
    return render(request, 'home/index.html',)
def dashboard(request):
    return render(request, 'home/dashboard.html')
def login(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        password = request.POST['password']

        user = auth.authenticate(username=userid, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Userid or password')
            ########return dashbord
            return redirect('login')
    else:

        return render(request, 'home/login.html')

def signup(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        usermail = request.POST['usermail']
        password = request.POST['password']
        password2 = request.POST['password2']
        # password verification
        if password == password2:
            ##check username
            if User.objects.filter(username=userid).exists():
                messages.error(request, 'Username is taken')
                return redirect('signup')
                
            else:               
                if User.objects.filter(email=usermail).exists():
                    messages.error(request, 'Usermail is taken')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=userid, password=password, email=usermail)
                    user.save()
                    messages.success(request, 'You are now Register')
                    return redirect('login')
        else:
            messages.error(request, "Password don't match")
            return redirect('signup')
    else:
        return render(request, 'home/signup.html')


def logout(request):
    django_logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

def profile(request):
    return render(request, 'home/profile.html')
        
