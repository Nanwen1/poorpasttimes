from django.urls import path
from django.urls import include, path
from . import views

app_name = 'users'

urlpatterns = [
    # users
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
]