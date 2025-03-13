from django.shortcuts import render
from .models import Notes , Sticky_notes
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages


def home(request):
    notes = Notes.objects.all()
    Snotes = Sticky_notes.objects.all()
    return render(request,"home.html",{"notes": notes, 
                                       "Snotes": Snotes})

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
    


