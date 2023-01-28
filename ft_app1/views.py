from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import UserRegisterForm

from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello HttpResponse</h1>')

def bar(request):
    return render(request,'ft_app1/navbar.html')
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