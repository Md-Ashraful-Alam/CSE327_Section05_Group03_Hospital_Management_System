from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response

from .models import Patient
from .models import Story
import mysql.connector
from operator import itemgetter
from django.contrib import messages

from .forms import Add_Story

from .forms import Add_Patient





def index(request):

    return render(request,'index.html')


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





def UpdatePatient(request, pk):
   
        pn=Patient.objects.get(patient_id=pk)
        fm=Add_Patient(instance=pn)

        if request.method== 'POST':
            fm=Add_Patient(request.POST, instance=pn)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
        return render(request, 'UpdatePatient.html', context)



def delete_patient(request, patient_id):

    if request.method=='POST':
        pi=Patient.objects.get(pk=patient_id)
        pi.delete()
        return HttpResponseRedirect('/')

def UpdateStory(request, pk):
   
        pn=Story.objects.get(patient_id=pk)
        fm=Add_Story(instance=pn)

        if request.method== 'POST':
            fm=Add_Story(request.POST, instance=pn)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
        return render(request, 'UpdateStory.html', context)



def delete_story(request, patient_id):

    if request.method=='POST':
        pi=Story.objects.get(pk=patient_id)
        pi.delete()
        return HttpResponseRedirect('/')



