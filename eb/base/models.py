from django.db import models

# Create your models here.
class Mt723(models.Model):
    date = models.DateField(unique=True)
    unit = models.IntegerField()
    session = models.IntegerField()
    
class Mt722(models.Model):
    date = models.DateField(unique=True)
    unit = models.IntegerField()
    session = models.IntegerField()
    
class Mt613(models.Model):
    date = models.DateField(unique=True)
    unit = models.IntegerField()
    session = models.IntegerField()
    
    
class sesion(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    
