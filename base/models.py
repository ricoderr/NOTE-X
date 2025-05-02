from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

class Notes(models.Model):
    Topic = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.Topic
    
    
class Sticky_notes(models.Model):
    Snote = models.CharField(max_length=100)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    history = HistoricalRecords()

    def __str__(self):
        return self.Snote
    

    
