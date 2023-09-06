from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
# Create your views here.
def login(request):
    if request.method == "POST":
        email= request.POST.get("email")
        password= request.POST.get("password")
        print(f'email is {email} and password is {password}')
        return render(request, "login.html") 
    else :
        return render(request, "login.html") 

def signup(request):
    if request.method == "POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        password= request.POST.get("password")
        return render(request, "signup.html") 
    else :
        return render(request, "signup.html") 


