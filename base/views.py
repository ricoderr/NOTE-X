from django.shortcuts import render, redirect
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
            return redirect("home")
            
        else :
            messages.error(request,"Crediantials error!")
            return render(request, "SignIn.html")
        
    return render(request, 'signIn.html')

def home(request):
    notes = Notes.objects.all()
    Snotes = Sticky_notes.objects.all()
    user = User.objects.all()
    if request.method =="POST":
        title_input = request.POST.get("title_input")
        discription_input = request.POST.get("discription_input")
        if title_input != "" and discription_input != "":
            Notes.objects.create(user = request.user ,Topic = title_input, discription = discription_input)
            messages.success(request, "Note added successfully")
        else: 
           messages.error(request, "Sorry! Invalid input") 
            
        
    return render(request,"home.html",{"notes": notes, 
                                       "Snotes": Snotes,
                                       "user": user})
    


