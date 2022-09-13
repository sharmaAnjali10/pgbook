from django.db import models
class Register1(models.Model):
   fname=models.CharField(max_length=100)
   lname=models.CharField(max_length=100)
   address=models.CharField(max_length=100)
   qualification=models.CharField(max_length=100)
   gender=models.CharField(max_length=100)
   lookingfor=models.CharField(max_length=100)
   no=models.CharField(max_length=100)
   email=models.CharField(max_length=100)
   pwd=models.CharField(max_length=100)
   cpwd=models.CharField(max_length=100)
   def __str__(self):
      return self.fname
class Register4(models.Model):
   fname=models.CharField(max_length=100)
   lname=models.CharField(max_length=100)
   address=models.CharField(max_length=100)
   gender=models.CharField(max_length=100)
   no=models.CharField(max_length=100)
   email=models.CharField(max_length=100)
   pwd=models.CharField(max_length=100)
   cpwd=models.CharField(max_length=100)
   def __str__(self):
      return self.fname
class Contact3(models.Model):
   name=models.CharField(max_length=100)
   email=models.CharField(max_length=100)
   msg=models.CharField(max_length=100)
   def __str__(self):
      return self.name
class Registerpg(models.Model):
   name=models.CharField(max_length=100)
   hno=models.CharField(max_length=100)
   address=models.CharField(max_length=100)
   sector=models.CharField(max_length=100)
   land=models.CharField(max_length=100)
   seats=models.CharField(max_length=100)
   room=models.CharField(max_length=100) 
   food=models.CharField(max_length=100)   
   email=models.CharField(max_length=100)
   photo=models.ImageField(upload_to='pgpics/')
   def __str__(self):
      return self.name
class Feed2(models.Model):
   name=models.CharField(max_length=100)
   email=models.CharField(max_length=100)
   msg=models.CharField(max_length=100)
   def __str__(self):
      return self.name
class Applypg(models.Model):
   pid=models.CharField(max_length=100)
   hno=models.CharField(max_length=100)
   address=models.CharField(max_length=100)
   sector=models.CharField(max_length=100)
   seats=models.CharField(max_length=100)
   photo=models.ImageField(upload_to='pgpics/')
   fname=models.CharField(max_length=100)
   email=models.CharField(max_length=100)
   no=models.CharField(max_length=100)
   def __str__(self):
      return self.pid
class Sendreq1(models.Model):
   pid=models.CharField(max_length=100)
   name=models.CharField(max_length=100)
   no=models.CharField(max_length=100)
   email=models.CharField(max_length=100)
   type=models.ImageField(upload_to='pgpics/')
   msg=models.CharField(max_length=500)
   p_name=models.CharField(max_length=100)
   p_email=models.CharField(max_length=100)
   rpy=models.CharField(max_length=500)
   def __str__(self):
      return self.pid	  	  
	  
	  

 