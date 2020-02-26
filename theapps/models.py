from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime, date


    
class ClassYear(models.Model):
    classyear = models.IntegerField(default=2019)

    def __str__(self):
        return "%s" % (self.classyear)
    
class Friends(models.Model):
    name = models.CharField(max_length=50)
    hobby = models.TextField()
    foods_drinks = models.TextField()
    classyear = models.ForeignKey(ClassYear, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name




#class Post(models.Model):
 #   yourname = models.CharField(max_length=50)
  #  classyear = models.IntegerField
   # hobby = models.TextField()

