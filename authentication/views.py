from product.models import insertProduct
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def authlogin(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        user = authenticate(request, username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
          messages.error(request, 'Invalid password or user name')

    return render(request,'authentication/login.html')

def authregister(request):
    if request.method == 'POST':
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User allready Exists')

            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email allready Exists')
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                return redirect('login')

        else:
            messages.error(request, 'Password does not match')

        
    return render(request,'authentication/register.html')


def authlogout(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login')