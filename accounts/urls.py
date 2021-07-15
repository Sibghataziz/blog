from django.urls import path
from .views import register
from django.contrib.auth import views


urlpatterns = [
    path('register/', register , name='register'),
    #path('register_success/', register, name="register_success"),
    path('login/', views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
]
