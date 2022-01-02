from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response

from .models import Medicine
from .models import Nurse
import mysql.connector
from operator import itemgetter
from django.contrib import messages
from .forms import Add_Nurse
from .forms import Add_Medicine


def index(request):

    return render(request,'index.html')
    




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





def UpdateMedicine(request, pk):
   
        pn=Medicine.objects.get(medicine_id=pk)
        fm=Add_Medicine(instance=pn)

        if request.method== 'POST':
            fm=Add_Medicine(request.POST, instance=pn)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
        return render(request, 'UpdateMedicine.html', context)



def delete_medicine(request, medicine_id):

    if request.method=='POST':
        pi=Medicine.objects.get(pk=medicine_id)
        pi.delete()
        return HttpResponseRedirect('/')




def UpdateNurse(request, pk):
   
        pn=Nurse.objects.get(nurse_id=pk)
        fm=Add_Nurse(instance=pn)

        if request.method== 'POST':
            fm=Add_Nurse(request.POST, instance=pn)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
        return render(request, 'UpdateNurse.html', context)



def delete_nurse(request, nurse_id):

    if request.method=='POST':
        pi=Nurse.objects.get(pk=nurse_id)
        pi.delete()
        return HttpResponseRedirect('/')




