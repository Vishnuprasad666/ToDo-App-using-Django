from django import forms
from todo.models import TodoModel

class TodoForm(forms.ModelForm):
    class Meta:
        model=TodoModel
        exclude=["status","user"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "last_date":forms.DateInput(attrs={"class":"form-control"}),
        }
    