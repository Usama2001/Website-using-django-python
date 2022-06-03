from datetime import date
import email
import numbers
from tokenize import Number

from django.db import models
from django.forms import Textarea

# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    Number =models.CharField(max_length=122)
    Textarea =models.TextField()
    date= models.DateField()

    def __str__(self):
        return self.name 


   