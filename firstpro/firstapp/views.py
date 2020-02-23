from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from firstapp import models
from .forms import UserRegisterForm,UserUpdateForm,formtable

def ind(request):
    return render(request,'ind.html')

def index2(request):
    dat=models.modeltable.objects.all()
    dic={'disp':dat}
    return render(request,'index2.html',context=dic)

def index(request):
    dat=models.modeltable.objects.all()
    dic={'disp':dat}
    return render(request,'index.html',context=dic)

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'register.html',{'form':form})

@login_required
def search(request,file):
    data=models.modeltable.objects.get(name=file)
    dict={'display':data}
    return render(request,'recipe.html',context=dict)

def searchfunc(request):
    if request.method=='POST':
        val=request.POST.get('element')
        data=models.modeltable.objects.get(name=val)
        dict={'display':data}
        return render(request,'recipe.html',context=dict)
    return render(request,'search.html')

@login_required
def addrecipe(request):
    formdata=formtable()
    if request.method=='POST':
        form=formtable(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'addrecipe.html',{'formdisplay':formdata})
