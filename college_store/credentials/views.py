from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, "form_link.html")
        else:
            messages.info(request, "Invalid username and password")
            return redirect('credentials:loginpage')

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']
        conf_password = request.POST['conf_password']

        if password == conf_password:

            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect("credentials:registerpage")
            else:
                user = User.objects.create_user(username=username, password=password)

                user.save()
                return redirect('credentials:loginpage')

        else:
            messages.info(request, "Password and confirm password are not same")
            return redirect("registerpage")

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
