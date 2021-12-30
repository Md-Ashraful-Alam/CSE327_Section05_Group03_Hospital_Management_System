from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from .models import User1
from .models import Appointment
from .models import Doctor
from .models import Test
import mysql.connector
from operator import itemgetter
from django.contrib import messages
from .forms import Add_Appointment
from .forms import Add_Doctor
from .forms import Add_Test


import os

from django.test import TestCase






def index(request):

    return render(request,'index.html')
    

def login(req):

    con=mysql.connector.connect(host="localhost",user="root",password="",database='hospital_management')
    cursor=con.cursor()
    con2=mysql.connector.connect(host="localhost",user="root",password="",database='hospital_management')
    cursor2=con2.cursor()
    sqlcommand="select username from service_user1"
    sqlcommand2="select password from service_user1"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)

    u=[]
    p=[]

    for i in cursor:
        u.append(i)
    for j in cursor2:
        p.append(j) 
    res=list(map(itemgetter(0),u))
    res2=list(map(itemgetter(0),p))
    print(res)
    #print(p)

    if req.method=="POST":
        username=req.POST['username']
        password=req.POST['password']
        i=1
        k=len(res)
        while i<k:
                if res[i]==username and res2[i]==password:
                    return render(req,'index.html',{'username':username})
                    break
                i=i+1
        else:
          messages.info(req, "Check username or password")
          return redirect("/")
    
  

    return render(req, 'login.html')
    User1()
    

def logout(request):

    return render(request, 'logout.html')


    
def register(req):
    if req.method=="POST":
        user=User1()

        user.username=req.POST['username']
        user.fname=req.POST['fname']
        user.lname=req.POST['lname']
        user.password=req.POST['password']
        user.repassword=req.POST['repassword']
        if user.password!=user.repassword:
            return redirect('register')
        elif user.fname=="" or user.password=="":
            messages.info(req, 'some fields are empty')
            return redirect('register')
        else:
            user.save()
    return render(req, 'register.html')


def appointments(request):
    apps=Appointment.objects.all()

    context={
        'apps': apps
    }
    return render(request, 'appointments.html', context)


def AddAppointment(request):
    if request.method== 'POST':
        fm=Add_Appointment(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Appointment()
    else:
      fm=Add_Appointment()
    return render(request, 'AddAppointment.html', {'form':fm})


def doctors(request):
    do=Doctor.objects.all()

    context={
        'do': do
    }
    return render(request, 'doctors.html', context)


def AddDoctor(request):
    if request.method== 'POST':
        fm=Add_Doctor(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Doctor()
    else:
      fm=Add_Doctor()
    return render(request, 'AddDoctor.html', {'form':fm})






def AddTest(request):
    if request.method== 'POST':
        fm=Add_Test(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Test()
    else:
      fm=Add_Test()
    return render(request, 'AddTest.html', {'form':fm})


def UpdateAppointment(request, pk):

    ap=Appointment.objects.get(appointment_id=pk)
        
    if request.method== 'POST':
            ap.appointment_id = request.POST.get('appointment_id')
            ap.patient_id = request.POST.get('patient_id')
            ap.doctor_id = request.POST.get('doctor_id')
            ap.appointment_date = request.POST.get('appointment_date')

            ap.save()
            messages.success(request, "Customer information updated Successfully")
            return redirect('/')

            
    context={'ap':ap}

    return render(request, 'UpdateAppointment.html', context)


def delete_datas(request, pk):
    if request.method=='POST':
        pt=Appointment.objects.get(appointment_id=pk)
        pt.delete()
        return HttpResponseRedirect('/')






def UpdateDoctor(request, pk):
   
        pn=Doctor.objects.get(doctorid=pk)
        fm=Add_Doctor(instance=pn)

        if request.method== 'POST':
            fm=Add_Doctor(request.POST, instance=pn)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
        return render(request, 'UpdateDoctor.html', context)



def delete_doctor(request, doctorid):

    if request.method=='POST':
        pi=Doctor.objects.get(pk=doctorid)
        pi.delete()
        return HttpResponseRedirect('/')





def UpdateTest(request, pk):
   
        pn=Test.objects.get(test_id=pk)
        fm=Add_Test(instance=pn)

        if request.method== 'POST':
            fm=Add_Test(request.POST, instance=pn)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
        return render(request, 'UpdateTest.html', context)



def delete_test(request, test_id):

    if request.method=='POST':
        pi=Test.objects.get(pk=test_id)
        pi.delete()
        return HttpResponseRedirect('/')

