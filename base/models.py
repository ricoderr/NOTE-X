from django.db import models

class Notes(models.Model):
    Topic = models.CharField(max_length=50)
    discription = models.TextField(max_length=1000)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.Topic
    
    
class Sticky_notes(models.Model):
    Snote = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.Snote
