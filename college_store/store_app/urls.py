from django.urls import path
from . import views

app_name="store_app"

urlpatterns = [
    path('', views.index, name="indexpage"),
    path('form/', views.form, name="formpage"),
    path('message/',views.message,name="messagepage"),



]
