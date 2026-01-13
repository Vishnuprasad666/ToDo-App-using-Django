from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TodoModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    last_date=models.DateField()
    status=models.CharField(max_length=50,default="Incomplete")
    user=models.ForeignKey(User,on_delete=models.CASCADE)