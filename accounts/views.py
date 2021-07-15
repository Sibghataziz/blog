from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .form import Register_form
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    # print(request.POST)
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        email= request.POST.get('email')
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if User.objects.filter(username__iexact=username).exists():
            messages.error(request,"Username already exist")
            return redirect("register")
        if User.objects.filter(email__iexact=email).exists():
            messages.error(request,"email already exist")
            return redirect("register")
        if pass1!=pass2:
            messages.error(request,"Password does not match")
            return redirect("register")
        
        myuser= User.objects.create(username=username, email=email)
        myuser.first_name= request.POST.get('First_Name')
        myuser.last_name= request.POST.get('Last_Name')
        myuser.set_password(pass1)
        myuser.save()
        messages.success(request,"Account have been created.")
        return redirect("login")
    else:
        form=Register_form
        return render(request,'accounts/register.html',{'form':form})



