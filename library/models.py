from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
        ]
    id =  models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'



