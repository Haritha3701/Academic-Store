from django.urls import path
from . import views

app_name = 'credentials'

urlpatterns = [
    path("login/", views.login, name="loginpage"),
    path('register/', views.register, name="registerpage"),
    path('logout/', views.logout, name="logoutpage"),

]
