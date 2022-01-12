from django.db import models
from django.conf import settings

class UserInfo(models.Model):
  NAME= models.CharField(max_length=50)
  EMAIL = models.EmailField()
  DATE = models.DateField(auto_now_add=True)

class UserCrashData(models.Model):
  OFFRNARR = models.TextField(null=True)
  CRSCATGRYINT=models.IntegerField(null=True)
  CRSCATGRY=models.CharField(max_length=50, null=True, blank=True)
  CRSHTYPE=models.IntegerField(null=True)
  INJSVR=models.CharField(max_length=1, null=True, blank=True)
  CRSHDATE = models.DateField(null=True)
  CRASHTIME=models.FloatField(null=True)  
  ONHWY=models.CharField(max_length=50, null=True, blank=True)
  ONSTR=models.CharField(max_length=50, null=True, blank=True)
  ATHWY=models.CharField(max_length=50, null=True, blank=True)
  ATSTR=models.CharField(max_length=50, null=True, blank=True)
  HWYCLASS=models.CharField(max_length=10, null=True, blank=True)  
  CNTYNAME=models.CharField(max_length=50, null=True, blank=True)
  MUNINAME=models.CharField(max_length=50, null=True, blank=True)
  MUNITYPE=models.CharField(max_length=50, null=True, blank=True)
  LATDECDG=models.DecimalField(max_digits=10,decimal_places=7, null=True, blank=True)
  LONDECDG=models.DecimalField(max_digits=10,decimal_places=7, null=True, blank=True)
 
 
  
class AdminCrashData(models.Model):
  OFFRNARR = models.TextField()
  CRSCATGRYINT=models.IntegerField()
  CRSCATGRY=models.CharField(max_length=50, null=True, blank=True)
  CRSHTYPE=models.IntegerField()
  INJSVR=models.CharField(max_length=1, null=True, blank=True)
  CRSHDATE = models.DateField()
  CRASHTIME=models.FloatField()  
  ONHWY=models.CharField(max_length=50, null=True, blank=True)
  ONSTR=models.CharField(max_length=50, null=True, blank=True)
  ATHWY=models.CharField(max_length=50, null=True, blank=True)
  ATSTR=models.CharField(max_length=50, null=True, blank=True)
  HWYCLASS=models.CharField(max_length=10, null=True, blank=True)  
  CNTYNAME=models.CharField(max_length=50, null=True, blank=True)
  MUNINAME=models.CharField(max_length=50, null=True, blank=True)
  MUNITYPE=models.CharField(max_length=50, null=True, blank=True)
  LATDECDG=models.DecimalField(max_digits=10,   decimal_places=7, null=True, blank=True)
  LONDECDG=models.DecimalField(max_digits=10,   decimal_places=7, null=True, blank=True)



  