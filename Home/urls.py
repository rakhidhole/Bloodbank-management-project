from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("",views.index, name='Home'),
    path("index",views.index, name='Home'),
    path("donation",views.donation, name='donation'),
    path("avail",views.avail, name='avail'),
    path("about",views.about, name='about'),
    path("guidelines",views.guidelines, name='guidelines'),
    path("saveRegistrationForm",views.saveRegistrationForm, name='saveRegistrationForm'),
    path("saveRegistrationForm",views.saveRegistrationForm, name='saveRegistrationForm'),
    
    

]
