#from django.db import models
from djongo import models
#import datetime
from django.core.validators import MinValueValidator , MaxValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Registrationform(models.Model):
    name=models.CharField(max_length=120)
    city=models.CharField(max_length=150)
    mobileno=models.CharField(max_length=12)
    bloodgroup_choice=[
        
        ('default','default'),
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-'), 
    ]
    bloodgroup= models.CharField(max_length=10, choices=bloodgroup_choice, default='default')
    units=models.PositiveIntegerField( 
        validators=[MinValueValidator(limit_value=1),MaxValueValidator(limit_value=10)],
    )
    Accepted='1'
    rejected='0'
    STATUS_chioce=[
    #    (False, _('0')),
    #    (True, _('1'))
    (Accepted,'accepted'),
    (rejected,'rejected'),
   ]
   

    
    STATUS= models.CharField(max_length=10,default='default', choices=STATUS_chioce)
    def conditional_value(self):
        if self.STATUS==self.Accepted:
            return"1"
        elif  self.STATUS==self.rejected:
            return"0"
    def __str__(self):
        return self.name
    
    
    #date=models.DateField()
class donors(models.Model): 
    _id= models.ObjectIdField()
    name=models.CharField(max_length=120)
    city=models.CharField(max_length=150)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=150)
    bloodgroup=models.CharField(max_length=150)
    unit=models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

    
        
    
        
    
        
    
