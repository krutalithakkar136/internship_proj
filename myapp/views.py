from typing import Any
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from myapp.models import Pract_Signup,Tasks,FurnitureInfo,Contact
import random
from django.core.mail import send_mail
from django.db.models import Q
from .forms import FurnitureCreate
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from qrcode import *
from django.contrib.auth import logout as logoutt,authenticate,login as log

from django.contrib.auth.decorators import login_required

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('')  # Redirect authenticated users to the home page
    else:
        return redirect('google_login')  # Redirect non-authenticated users to the Google login page
    

def google_callback(request):
    return redirect('/')

data=None
def qr_gen(request):
    global data
    if request.method=="POST":
        data=request.POST['data']
        img=make(data)
        print("---------------------",img)
        img.save("myapp/static/images/test.png")
        return render(request,"qr_gen.html",{'data':data})

    else:
        pass
    return render(request,"qr_gen.html",{'data':data})


def signup(request):
    if request.method=="POST":
        try: 
            Pract_Signup.objects.get(email=request.POST['email'])
            msg="Email Already Registered"
            return render(request,'signup.html',{'msg':msg})
        except:
            Pract_Signup.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                phone=request.POST['phone'],
                address=request.POST['address'],
                password=request.POST['password'],
            )
        user=Pract_Signup.objects.all()
        msg="Signup Successful"
        return render(request,'signup.html',{'user':user,'msg':msg})
    else:
        return render(request,'signup.html')
    
def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def shop(request):
    return render(request,'shop.html')

def index(request):
    return render(request,'index.html')

def add_click(request):
    if request.method=="POST":
        Tasks.objects.create(
            t_name=request.POST['t_name'],
            t_desc=request.POST['t_desc'],
            cat=request.POST['cat'],
            status=request.POST['status'],
        )
        return redirect('add_btn')
    else:
        category_list = Tasks.objects.all()
        return render(request,'add_click.html', {"category_list": category_list})
    
def add_btn(request):
    item_list = Tasks.objects.order_by("-date")
    if request.method=="POST":
        page = {
            "list": item_list,
            "title": "TODO LIST",
        }
        return render(request, 'add_btn.html', page)
    else:
        page = {
            "list": item_list,
            "title": "TODO LIST",
        }
        return render(request,'add_btn.html', page)

def login(request):
    if request.method=='POST':
        try:
            # user=Pract_Signup.objects.get(email=request.POST['email'])
            user = authenticate(email = request.POST['email'],password = request.POST['password'])
            if user:
                log(request=request,user=user)
                # request.session['email']=user.email
                return render(request,'index.html')
            else:
                msg="Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        except:
            msg="Email not registered"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
    
def logout(request):
    logoutt(request)
    return redirect('/login/')
    
def change_password(request):
    if request.method=='POST':
        user=Pract_Signup.objects.get(email=request.session['email'])
        if user.password==request.POST['old_password']:
            if request.POST["new_password"]==request.POST["cnew_password"]:
                user.password=request.POST['new_password']
                user.save()
                return redirect('logout')
            else:
                msg="New Password And Confirm New Password Does Not Match"
                return render(request,'change_password.html',{'msg':msg})
        else:
            msg="Old Password Not Matched"
            return render(request,'change_password.html',{'msg':msg})
    else:
        return render(request,'change_password.html')
    

def forgot_password(request):
    if request.method=="POST":
        try:
            user=Pract_Signup.objects.get(email=request.POST['email'])
            otp=random.randint(1000,9999)
            subject="OTP For Forgot Password"
            message="Hello "+user.name+',Your OTP is'+str(otp)
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[user.email,]
            send_mail(subject,message,email_from,recipient_list)
            return render(request,'otp.html',{'email':user.email,'otp':otp})
        except:
            msg="Email Id Not Found"
            return render(request,'forgot_password.html',{'msg':msg})
    return render(request,'forgot_password.html')


def verify_otp(request):
    email=request.POST['email']
    otp=request.POST['otp']
    uotp=request.POST['uotp']
    if uotp==otp:
        return render(request,'new_password.html',{'email':email})
    else:
        msg="Invalid OTP"
        return render(request,'otp.html',{'email':email,'otp':otp,'msg':msg})

def new_password(request):
    email=request.POST['email']
    np=request.POST['new_password']
    cnp=request.POST['cnew_password']
    if np==cnp:
        user=Pract_Signup.objects.get(email=email)
        if user.password==np:
            msg="You cannot use your old password"
            return render(request,'new_password.html',{'email':email,'msg':msg})
        else:
            user.password=np
            user.save()
            msg="Password Updated Successfully"
            return render(request,'login.html',{'msg':msg})
    else:
        msg="New password and Confirm new password Does Not Match"
        return render(request,'new_password.html',{'email':email,'msg':msg})
    


def create_view(request):
    context ={}
 
    form = FurnitureCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_view/')
    context['form']= form
    return render(request, "create_view.html", context)


def list_view(request):
    context ={}
    if request.method=="POST":
        search_query = request.POST['search_query']
        context['data'] = FurnitureInfo.objects.filter(Q(Furniture_name__icontains=search_query)|Q(Furniture_modelno__icontains=search_query)|Q(Furniture_desc__icontains=search_query)|Q(Furniture_cat__icontains=search_query)).values()
        return render(request, 'list_view.html', context)
    else:
        context['data'] = FurnitureInfo.objects.all()
        return render(request, "list_view.html", context)


def detail_view(request, id):
    context ={}

    context["data"] = FurnitureInfo.objects.get(id = id)
         
    return render(request, "detail_view.html", context)     

def update_view(request, id):
    context ={} 
    obj = FurnitureInfo.objects.get(id=id)
    form = FurnitureCreate(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list_view")
    
    context["form"] = form
    return render(request, "update_view.html", context)

def delete_view(request,id):
    context={}
    obj=FurnitureInfo.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return HttpResponseRedirect("/list_view")
    else:
        return render(request,'delete_view.html',context)
    

def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
            )
        user=Contact.objects.all()
        msg="Message Sent Successfully"
        return render(request,'contact.html',{'user':user,'msg':msg})
    else:
        return render(request,'contact.html')