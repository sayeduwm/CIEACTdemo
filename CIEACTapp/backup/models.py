from django.db import models
from django.conf import settings



class AdminDatabase(models.Model):
  EMAIL=models.EmailField( null=True)
  DATAID=models.CharField(max_length=3, null=True, blank=True)
  CRSHNMBR=models.IntegerField(default=999,primary_key=True)
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
  UNIPRO=models.DecimalField(max_digits=6,decimal_places=5,null=True)
  BIPRO=models.DecimalField(max_digits=6,decimal_places=5,null=True)
  TRIPRO=models.DecimalField(max_digits=6,decimal_places=5,null=True)   
  
class UserDatabase(models.Model):
  EMAIL=models.EmailField(null=True)
  DATAID=models.CharField(max_length=3, null=True, blank=True)
  CRSHNMBR=models.IntegerField(default=999,primary_key=True)  
  #CRSCATGRYINT=models.IntegerField(null=True)
  #CRSCATGRY=models.CharField(max_length=50, null=True, blank=True)
  #CRSHTYPE=models.IntegerField(null=True)
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
  OFFRNARR = models.TextField(max_length=1000,null=True)  
  NOISYORU=models.DecimalField(max_digits=6,decimal_places=5,null=True)
  NOISYORB=models.DecimalField(max_digits=6,decimal_places=5,null=True)
  NOISYORT=models.DecimalField(max_digits=6,decimal_places=5,null=True)
  NOISYORUB=models.DecimalField(max_digits=6,decimal_places=5,null=True)
  POSUNIGRAM=models.CharField(max_length=300, null=True, blank=True)
  POSBIGRAM=models.CharField(max_length=300, null=True, blank=True)
  POSTRIGRAM=models.CharField(max_length=300, null=True, blank=True)
    
  
  
class UserInfoDatabase(models.Model):
  NAME= models.CharField(max_length=50)
  EMAIL = models.EmailField(primary_key=True)
  DATE = models.DateField(auto_now_add=True)
  
class UserQuery(models.Model):
  MODELNAME=models.CharField(max_length=50)
  
class WorkzoneUnigram(models.Model):
  Unigrams=models.CharField(max_length=30, null=True, blank=True)
  Probability= models.DecimalField(max_digits=6,decimal_places=5, null=True, blank=True)


class WorkzoneBigram(models.Model):
  Bigrams=models.CharField(max_length=30, null=True, blank=True)
  Probability= models.DecimalField(max_digits=6,decimal_places=5, null=True, blank=True)

  
class WorkzoneTrigram(models.Model):
  Trigram=models.CharField(max_length=60, null=True, blank=True)
  Probability= models.DecimalField(max_digits=6,decimal_places=5, null=True, blank=True)


# Distracted Driving
class DistractedUnigram(models.Model):
  Unigrams=models.CharField(max_length=30, null=True, blank=True)
  Probability= models.DecimalField(max_digits=6,decimal_places=5, null=True, blank=True)


class DistractedBigram(models.Model):
  Bigrams=models.CharField(max_length=30, null=True, blank=True)
  Probability= models.DecimalField(max_digits=6,decimal_places=5, null=True, blank=True)

  
class DistractedTrigram(models.Model):
  Trigram=models.CharField(max_length=60, null=True, blank=True)
  Probability= models.DecimalField(max_digits=6,decimal_places=5, null=True, blank=True)

  
# Distracted Driving
class InattentiveUnigram(models.Model):
  Unigrams=models.CharField(max_length=30, null=True, blank=True)
  Probability= models.DecimalField(max_digits=6,decimal_places=5, null=True, blank=True)


class InattentiveBigram(models.Model):
  Bigrams=models.CharField(max_length=30, null=True, blank=True)
  Probability= models.DecimalField(max_digits=6,decimal_places=5, null=True, blank=True)

  
class InattentiveTrigram(models.Model):
  Trigram=models.CharField(max_length=60, null=True, blank=True)
  Probability= models.DecimalField(max_digits=6,decimal_places=5, null=True, blank=True)
