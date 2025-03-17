from django.shortcuts import render
from .models import Notes , Sticky_notes
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate, login


def signUp(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        Email = request.POST.get("Email")
        Password = request.POST.get("Password")
        Cpassword = request.POST.get('Cpassword')
        if Password != Cpassword:
            return render(request,'signUp.html',{'error': "passwords doesn't match"})
        try: 
            myuser = User.objects.create_user(Username,Email,Password) 
            myuser.save()
            messages.success(request, "User created successfully")
        except IntegrityError:
            return render(request,'signUp.html',{'error': "User already exists!"})
            
            
    return render(request,"signUp.html", {"messages" : messages})

def signIn(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        pass1 = request.POST.get("password")
        user = authenticate(username = username , password = pass1)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome back!")
            return render(request, "home.html", {"messages" : messages})
            
        else :
            messages.error(request,"Crediantials error!")
            return render(request, "SignIn.html")
        
    return render(request, 'signIn.html')

def home(request):
    notes = Notes.objects.all()
    Snotes = Sticky_notes.objects.all()
    return render(request,"home.html",{"notes": notes, 
                                       "Snotes": Snotes})
    


