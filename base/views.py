from django.shortcuts import render
from .models import Notes , Sticky_notes

def home(request):
    notes = Notes.objects.all()
    Snotes = Sticky_notes.objects.all()
    return render(request,"home.html",{"notes": notes, 
                                       "Snotes": Snotes})
    


