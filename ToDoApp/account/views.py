from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from account.forms import UserRegForm,CustomUserForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class UserRegView(View):
    def get(self,request):
        # form=UserRegForm()
        # form=UserCreationForm()
        form=CustomUserForm()
        return render(request,"reg.html",{"form":form})
    def post(self,request,**kwargs):
        # form_data=UserRegForm(data=request.POST)
        # form_data=UserCreationForm(data=request.POST)
        form_data=CustomUserForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('loginpage')
        return render(request,'reg.html',{"form":form_data})

class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")  
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"Login Successfull!!")
                return redirect('uhome')
            else:
                messages.warning(request,"Invalid Username or Password")
                return redirect('loginpage')
        messages.error(request,"Invalid Input Recieved!!")
        return render(request,"login.html",{"form":form_data})

class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"User Logged Out!")
        return redirect('loginpage')
