from django.shortcuts import render
from .models import Department, Course


# Create your views here.


def index(request):
    dept = Department.objects.all()
    return render(request, 'index.html', {"dept": dept})


def form(request):
    dept = Department.objects.all()
    course = Course.objects.all()

    return render(request, "form.html", {"dept": dept, "course": course})


def message(request):
    return render(request, 'message.html')


