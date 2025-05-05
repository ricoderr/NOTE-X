from django.shortcuts import render, redirect
from .models import Notes , Sticky_notes
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from itertools import chain
from operator import attrgetter


def home(request):
    combined_history = []
    if request.user.is_authenticated:
        notes = Notes.objects.filter(user = request.user)
        Snotes = Sticky_notes.objects.filter(user = request.user)
        
        if request.method =="POST":
            title_input = request.POST.get("title_input")
            description_input = request.POST.get("description_input")
            Snote = request.POST.get("Stitle_input")
            if title_input and description_input: 
                if title_input != "" and description_input != "":
                    Notes.objects.create(user = request.user ,Topic = title_input, description = description_input)
                    messages.success(request, "Note added successfully")
                else: 
                    messages.error(request, "Sorry! Invalid input") 
            if Snote: 
                if Snote != "": 
                    Sticky_notes.objects.create(user = request.user, Snote = Snote)
                    messages.success(request, "Sticky Note added successfully")
                else: 
                    messages.error(request, "Sorry! Invalid input")
            return redirect('home')
        note_history = Notes.history.filter(user = request.user).all()
        snote_history = Sticky_notes.history.filter(user = request.user).all()
           
        combined_history = sorted(
        chain(note_history, snote_history),
        key=attrgetter('history_date'),
        reverse=True 
        )
            
        
    else:
        notes = None
        Snotes = None 
        
            
        
    return render(request,"home.html",{"notes": notes, 
                                       "Snotes": Snotes,
                                       "user":request.user, 
                                       "history":combined_history})
    

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

def Logout(request):
    logout(request)
    messages.success(request, "You have been logged out succesfully!")
    return redirect('signIn')
