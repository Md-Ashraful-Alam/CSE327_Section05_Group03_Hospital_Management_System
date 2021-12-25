from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .models import User1
from .models import Appointment
from .models import Bed
from .models import Patient
from .models import Doctor
from .models import Test
from .models import Medicine
from .models import BloodDonate
from .models import OrganDonate
from .models import Story
from .models import Nurse
import mysql.connector
from operator import itemgetter
from django.contrib import messages
from .forms import Add_Appointment
from .forms import Add_Bed
from .forms import Add_Story
from .forms import Add_Nurse
from .forms import Add_Patient
from .forms import Add_Doctor
from .forms import Add_Test
from .forms import Add_OrganDonate
from .forms import Add_BloodDonate
from .forms import Add_Medicine

import os


# Create your views here.



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
        user=User()

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

def beds(request):
    be=Bed.objects.all()

    context={
        'be': be
    }
    return render(request, 'beds.html', context)


def AddBed(request):
    if request.method== 'POST':
        fm=Add_Bed(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Bed()
    else:
      fm=Add_Bed()
    return render(request, 'AddBed.html', {'form':fm})


def bloods(request):
    bl=BloodDonate.objects.all()

    context={
        'bl': bl
    }
    return render(request, 'bloods.html', context)


def AddBlood(request):
    if request.method== 'POST':
        fm=Add_BloodDonate(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_BloodDonate()
    else:
      fm=Add_BloodDonate()
    return render(request, 'AddBlood.html', {'form':fm})


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


def medicines(request):
    me=Medicine.objects.all()

    context={
        'me': me
    }
    return render(request, 'medicines.html', context)


def AddMedicine(request):
    if request.method== 'POST':
        fm=Add_Medicine(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Medicine()
    else:
      fm=Add_Medicine()
    return render(request, 'AddMedicine.html', {'form':fm})


def nurses(request):
    nu=Nurse.objects.all()

    context={
        'nu': nu
    }
    return render(request, 'nurses.html', context)


def AddNurse(request):
    if request.method== 'POST':
        fm=Add_Nurse(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Nurse()
    else:
      fm=Add_Nurse()
    return render(request, 'AddNurse.html', {'form':fm})



def organs(request):
    org=OrganDonate.objects.all()

    context={
        'org': org
    }
    return render(request, 'organs.html', context)


def AddOrgan(request):
    if request.method== 'POST':
        fm=Add_OrganDonate(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_OrganDonate()
    else:
      fm=Add_OrganDonate()
    return render(request, 'AddOrgan.html', {'form':fm})

def patients(request):
    pa=Patient.objects.all()

    context={
        'pa': pa
    }
    return render(request, 'patients.html', context)


def AddPatient(request):
    if request.method== 'POST':
        fm=Add_Patient(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Patient()
    else:
      fm=Add_Patient()
    return render(request, 'AddPatient.html', {'form':fm})

def tests(request):
    te=Test.objects.all()

    context={
        'te': te
    }
    return render(request, 'tests.html', context)


def AddTest(request):
    if request.method== 'POST':
        fm=Add_Test(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Test()
    else:
      fm=Add_Test()
    return render(request, 'AddTest.html', {'form':fm})

def stories(request):
    st=Story.objects.all()

    context={
        'st': st
    }
    return render(request, 'stories.html', context)


def AddStory(request):
    if request.method== 'POST':
        fm=Add_Story(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Story()
    else:
      fm=Add_Story()
    return render(request, 'AddStory.html', {'form':fm})





