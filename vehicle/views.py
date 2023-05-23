from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from vehicle.forms import *
from django.contrib import messages 
from django.contrib.auth import login
# Create your views here.

class homeview(TemplateView):
    template_name="homepage.html"
class contactview(TemplateView):
    template_name="contact.html"
def about_usview(request):
    
    return render(request,"about_us.html")
def gallaryview(request):
    gal=gallary.objects.all()
    return render(request,"gallary.html",{'gal':gal})
class servicesview(TemplateView):
    template_name="services.html"
def faqview(request):
    f=faq.objects.all()
    return render(request,"faq.html",{'f':f})
class registractionview(TemplateView):
    template_name="registraction.html"


def blogsview(request):
    blg=blog.objects.all()
    return render(request,"blogs.html",{'blg':blg})

def blogdetailview(request,id):
    b=blog.objects.get(id=id)
    return render(request,"blogdetail.html",{'b':b})






def signupview(request):
    if request.method=='post':
        forms=signupform(request.post)
        if forms.is_valid():
            user=forms.save()
            login(request,user)
            return redirect('/blogs/')
    else:
         form=signupform()
    return render(request,"registration/signup.html",{'form':form})     
              

def insertcontact(request):
    if request.method=="POST":
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent.')
            return redirect('/contact/')
    else:
         form=contactform()
    return render(request,"contact.html",{'form':form})   

def insertservices(request):
    if request.method=='POST':
        form=servicesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/services/')
    else:
         form=servicesform()
    return render(request,"services.html",{'form':form}) 
 

def insertappointment(request):
    if request.method=='POST':
        form=appointmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/appointment/')
    else:
         form=appointmentform()
    return render(request,"appointment.html",{'form':form}) 
def appointmentview(request):
    return render(request,"appointment.html")

def insertdisplayappointment(request):
 def displayappointmentview(request):
    return render(request,"displayappointment.html")