from django.shortcuts import render
from django.contrib.auth import authenticate #new
from django.contrib.auth import login
from django.shortcuts import redirect #new
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
# Create your views here.


def homepage(request):
    return render(request, "index.html")

def signinpage(request):
    print("you did a " + request.method)
    if request.method == "POST":
        print( request.POST ) #new 
        typedname = request.POST.get ("username")
        print("The name you typed is: "+ typedname)
        typedpassword = request.POST.get ("password")
        result = authenticate(username = typedname, password = typedpassword) 
        if result == None :
            return HttpResponse("You aren't registerd with us")
        else:
            login(request, result)
            return redirect("homepage")
    return render(request, "signin.html")


def signup(request):
    if request.method == "POST":
        typedname = request.POST.get ("username")
        typedpassword = request.POST.get ("password")
        typedemail = request.POST.get ("email")
        typedfirstname = request.POST.get ("firstname")
        typedlastname = request.POST.get ("lastname")
        new_password = make_password(typedpassword)
        new_user = User(username=typedname,password=new_password,email=typedemail,first_name=typedfirstname,last_name=typedlastname)
        new_user.save()
        return redirect("signinpage")
    return render(request, "signup.html")


def signout(request):
    logout(request)
    return redirect("signinpage")


def destination(request):
    return render(request, "destinations.html")
