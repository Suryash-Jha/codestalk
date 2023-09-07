from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def loginx(request):
    if request.method == "POST":
        useremail = request.POST.get("email")
        passw = request.POST.get("password")
        # print(email + " " + passw)
        user = authenticate(request, username=useremail, password=passw)
        if user:
            login(request, user)
            print("success")
        else:
            print("failure")

        # alldata= User.objects.all()
        # print(alldata[0].password)
        return render(request, "login.html")
    else:
        return render(request, "login.html")


def logoutx(request):
    logout(request)
    return HttpResponse("Successfully LoggedOut")



def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        p = User.objects.create_user(email, name, password)
        p.save()
        return render(request, "login.html")
    else:
        return render(request, "signup.html")
