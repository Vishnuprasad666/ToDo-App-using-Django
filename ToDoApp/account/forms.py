from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]

class CustomUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username"]
        widgets={
            "first_name":forms.TextInput(attrs={"placeholder":"Enter First Name","class":"form-control bg-secondary text-info"}),
            "last_name":forms.TextInput(attrs={"placeholder":"Enter Last Name","class":"form-control"}),
            "email":forms.EmailInput(attrs={"placeholder":"Enter Email ID","class":"form-control"}),
            "username":forms.TextInput(attrs={"placeholder":"Enter Userame","class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"placeholder":"Enter Password","class":"form-control"}),
            "password2":forms.PasswordInput(attrs={"placeholder":"Re-Enter Password","class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))