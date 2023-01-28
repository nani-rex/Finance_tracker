from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import UserRegisterForm
from .models import Income
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    return render(request,'ft_app1/home.html')

@login_required
def bar(request):
    return render(request,'ft_app1/navbar.html')

@login_required
def addinc(request):
    if request.method=='POST':
        cat=request.POST.get('description')
        amtt=request.POST.get('amount')
        datee=request.POST.get('date')
        idd= request.user
        income=Income.objects.create(catg=cat,amt=amtt,date=datee,author=idd)
        income.save()
    return render(request,'ft_app1/add_income.html')

@login_required
def viewinc(request):
    usser=request.user
    icome = {
        'inci':Income.objects.all()
        }
    return render(request,'ft_app1/view_income.html',icome)

@login_required
def viewexp(request):
    return render(request,'ft_app1/view_expense.html')

@login_required
def viewrem(request):
    return render(request,'ft_app1/view_reminder.html')

@login_required
def addrem(request):
    return render(request,'ft_app1/add_reminder.html')

@login_required
def addexp(request):
    return render(request,'ft_app1/add_expense.html')

@login_required
def uprof(request):
    return render(request,'ft_app1/u_profile.html')

def regiister(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'ft_app1/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'ft_app1/profile.html')