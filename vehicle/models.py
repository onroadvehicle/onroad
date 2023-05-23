from django.db import models
from tinymce.models import HTMLField
import datetime
# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    message=models.TextField()
    class Meta:
        db_table="contact"
        
class services(models.Model):
    Name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    message=models.TextField()
    class Meta:
        db_table="services"

class faq(models.Model):
    question=models.TextField()
    answer=models.TextField()
    class Meta:
        db_table="faq"
    def __str__(self):
        return  self.question
    
class gallary(models.Model):
    photos=models.ImageField(upload_to='gallery/')
    #answer=models.TextField()
    class Meta:
        db_table="gallary"

class blog(models.Model):
    tittle=models.CharField(max_length=100)
    description=HTMLField()
    photo=models.ImageField(upload_to='blog/')
    postby=models.CharField(max_length=50,default="Admin")
    poston=models.DateField(default=datetime.date.today())
    class Meta:
        db_table="blogs"
    def __str__(self):
        return self.tittle
    
class appointment(models.Model):
    name=models.CharField(max_length=20,default="")
    location=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    vehicletype=models.CharField(max_length=50)
    vehiclenumber=models.CharField(max_length=50,default="")
    vehicleservices=models.CharField(max_length=50,default="")
    message=models.TextField(default="")
    
    class Meta:
        db_table="appointment"   
    
   
    



