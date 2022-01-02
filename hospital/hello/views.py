from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response

from .models import Bed
from .models import BloodDonate
import mysql.connector
from operator import itemgetter
from django.contrib import messages

from .forms import Add_Bed

from .forms import Add_BloodDonate




def index(request):

    return render(request,'index.html')
    

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





def UpdateBed(request, pk):
   
        ps=Bed.objects.get(bed_id=pk)
        fm=Add_Bed(instance=ps)

        if request.method== 'POST':
            fm=Add_Bed(request.POST, instance=ps)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
        return render(request, 'UpdateBed.html', context)



def delete_datam(request, pk):

    if request.method=='POST':
        pt=Bed.objects.get(bed_id=pk)
        pt.delete()
        return HttpResponseRedirect('/')





def UpdateBlood(request, pk):
   
        pn=BloodDonate.objects.get(patient_id=pk)
        fm=Add_BloodDonate(instance=pn)

        if request.method== 'POST':
            fm=Add_BloodDonate(request.POST, instance=pn)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
        return render(request, 'UpdateBlood.html', context)



def delete_blood(request, patient_id):

    if request.method=='POST':
        pi=BloodDonate.objects.get(pk=patient_id)
        pi.delete()
        return HttpResponseRedirect('/')



