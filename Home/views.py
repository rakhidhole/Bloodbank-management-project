from django.shortcuts import render,HttpResponse
from Home.models import Registrationform
from Home.models import donors



# Create your views here.
def index(request):
    return render(request,'index.html')

def donation(request):
    return render(request,'donation.html') 
def avail(request):
    dict={
        'A1': donors.objects.all().filter(bloodgroup='A+').count(),
        'A2': donors.objects.all().filter(bloodgroup='A-').count(),
        'B1': donors.objects.all().filter(bloodgroup='B+').count(),
        'B2': donors.objects.all().filter(bloodgroup='B-').count(),
        'AB1': donors.objects.all().filter(bloodgroup='AB+').count(),
        'AB2': donors.objects.all().filter(bloodgroup='AB-').count(),
        'O1' : donors.objects.all().filter(bloodgroup='O+').count(),
        'O2' : donors.objects.all().filter(bloodgroup='O-').count(),
        'a' : Registrationform.objects.all().filter(STATUS='1').count(),
        'b':Registrationform.objects.all().count(),
        'c': donors.objects.all().filter(bloodgroup='A+').count()+donors.objects.all().filter(bloodgroup='A-').count()+donors.objects.all().filter(bloodgroup='B+').count()+donors.objects.all().filter(bloodgroup='B-').count()+ donors.objects.all().filter(bloodgroup='AB+').count()+ donors.objects.all().filter(bloodgroup='AB-').count()+donors.objects.all().filter(bloodgroup='O+').count()+ donors.objects.all().filter(bloodgroup='O-').count(),
    }
   
    return render(request,'avail.html',context=dict,)

def about(request):
    return render(request,'about.html')

def guidelines(request):
    return render(request,'guidelines.html')

def saveRegistrationForm(request):
    if request.method =="POST":
        name=request.POST.get("name")
        city=request.POST.get("city")
        mobileno=request.POST.get("mobileno")
        bloodgroup=request.POST.get("bloodgroup")
        units=request.POST.get("units")
        en=Registrationform(name=name,city=city,mobileno=mobileno,bloodgroup=bloodgroup,units=units,)
        en.save()
      

            
        
        
    
    return render(request,'saveRegistrationForm.html')
