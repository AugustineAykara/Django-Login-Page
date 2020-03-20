from django.shortcuts import render, redirect

# user model object for user object and authentication
from django.contrib.auth.models import User, auth 
# for print message
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if password == confirmPassword:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                return redirect('login')
            
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
