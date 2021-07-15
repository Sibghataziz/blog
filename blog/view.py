from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from post.views import home_view

def web_home(request):
    if request.user.is_authenticated:
        return redirect("home")
      
    return render(request,'web_home.html')