from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response

from .models import OrganDonate
from .models import User
import mysql.connector
from operator import itemgetter
from django.contrib import messages
from .forms import Add_OrganDonate
from .forms import Add_User


def index(request):

    return render(request,'index.html')
    



def AddOrgan(request):
    if request.method== 'POST':
        fm=Add_OrganDonate(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_OrganDonate()
    else:
      fm=Add_OrganDonate()
    return render(request, 'AddOrgan.html', {'form':fm})


def users(request):
    us=User.objects.all()

    context={
        'us': us
    }
    return render(request, 'users.html', context)


def AddUser(request):
    if request.method== 'POST':
        fm=Add_User(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_User()
    else:
      fm=Add_User()
    return render(request, 'AddUser.html', {'form':fm})



def UpdateOrgan(request, pk):
   
        pn=OrganDonate.objects.get(nurse_id=pk)
        fm=Add_OrganDonate(instance=pn)

        if request.method== 'POST':
            fm=Add_OrganDonate(request.POST, instance=pn)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
        return render(request, 'UpdateOrgan.html', context)



def delete_organ(request, patient_id):

    if request.method=='POST':
        pi=OrganDonate.objects.get(pk=patient_id)
        pi.delete()
        return HttpResponseRedirect('/')




def UpdateUser(request, pk):
   
        pn=User.objects.get(user_id=pk)
        fm=Add_User(instance=pn)

        if request.method== 'POST':
            fm=Add_User(request.POST, instance=pn)
            if fm.is_valid():
                fm.save()
                return redirect('/')

        context={'form':fm}
        
        return render(request, 'UpdateUser.html', context)



def delete_user(request, user_id):

    if request.method=='POST':
        pn=User.objects.get(pk=user_id)
        pn.delete()
        return HttpResponseRedirect('/')

