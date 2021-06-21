from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')



def register(reguest):
    if reguest.method=='POST':
        first_name = reguest.POST['first_name']
        last_name = reguest.POST['last_name']
        username = reguest.POST['username']
        password1 = reguest.POST['password1']
        password2 = reguest.POST['password2']
        email = reguest.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(reguest,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(reguest,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print("user created")
        else:
            print("incorrect password")
            return redirect('register')
        return redirect('/')

    else:
        return render(reguest,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')