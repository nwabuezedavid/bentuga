from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render,redirect
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User  # To associate with Django's built-in User model
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
from .form import ContactForm
# Create your views here.
def home(request):
     
    con ={
        "site":siteedit.objects.get(idx = 1),
        
    }
    return render (request, "home/home.html",con)
def about(request):
     
    con ={
        "site":siteedit.objects.get(idx = 1),
        
    }
    return render (request, "home/about.html",con)
def service(request):
     
    con ={
        "site":siteedit.objects.get(idx = 1),
        
    }
    
    return render (request, "home/service.html",con)
def invest(request):
     
    con ={
        "site":siteedit.objects.get(idx = 1),
        
    }
    
    return render (request, "home/invest.html",con)
def grant(request):
     
    con ={
        "site":siteedit.objects.get(idx = 1),
        
    }
    
    return render (request, "home/grant.html",con)
def coverage(request):
     
    con ={
        "site":siteedit.objects.get(idx = 1),
        
    }
    
    return render (request, "home/coverage.html",con)
def capital(request):
     
    con ={
        "site":siteedit.objects.get(idx = 1),
        
    }
    
    return render (request, "home/capital.html",con)
def contact(request):
     
    con ={
        "site":siteedit.objects.get(idx = 1),
        
    }
    
    return render (request, "home/contact.html",con)
def qoute(request):
    statue = None
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            ip_address = request.POST.get('ip')
            form.instance.ip_address = ip_address
            form.save()
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            files = form.cleaned_data['files']
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
             
            sitex=siteedit.objects.get(idx=1)
            print(sitex.owneremail )
            statue = messages.info( request,'Your message has been sent!')
            conx={
                              'site':sitex,
                              'email':email,
                              'phone':phone,
                              'files':files,
                              'subject':subject,
                              'message':message,
                              'name':name,
                              'ip_address':ip_address,
                              
                              
                         }
            email_sending(request,"./mail/Consulting.html",conx,f"Your submission received",f"{email.replace(" ", "")
     }")
            email_sending(request,"./mail/detail.html",conx,f"Your submission received",f"{sitex.owneremail.replace(" ", "")
     }")
            return redirect('qoute') 
        else:
            statue = messages.info(request,  form.errors)
    else:
        form = ContactForm()
     
    con ={
        "site":siteedit.objects.get(idx = 1),
        'form': form,
        'statue': statue,
    }
    
    return render (request, "home/form.html",con)
from django.core.mail import send_mail,  EmailMultiAlternatives
from  django.utils.html import strip_tags
from django.conf import settings
from django.template.loader import get_template, render_to_string
def email_sending(request,tempname,context,subjects,to):
    tos = render_to_string(tempname,context=context )
    tags =strip_tags(tos)
    mas = EmailMultiAlternatives(
        subject = subjects,
        body=tags,
        from_email = settings.EMAIL_HOST_USER,
        to=[to]
    )
    mas.attach_alternative(tos, 'text/html')
    mas.send()
 