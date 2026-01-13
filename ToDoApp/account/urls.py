from django.urls import path
from account.views import *


urlpatterns=[
    path('userregistration',UserRegView.as_view(),name='reguser'),
    path('login',LoginView.as_view(),name='loginpage'),
    path('logout',LogoutView.as_view(),name='logout')
]