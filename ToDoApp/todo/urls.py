from django.urls import path
from todo.views import *


urlpatterns=[
    path('userhome',UserHomeView.as_view(),name='uhome'),
    path('addtodo',AddTodoView.as_view(),name='addtodo'),
    path('todolist',TodoListView.as_view(),name='tdlist'),
    path('tododelete/<int:tdid>',TodoDeleteView.as_view(),name='tddelete'),
    path('statusupdate/<int:tdid>/<str:status>',StatusUpdateView.as_view(),name='statusupdate'),
    # path('todocancel/<int:tdid>',TodoCancelView.as_view(),name='canceltodo'),
    path('edittodo/<int:tdid>',EditTodoView.as_view(),name='todoedit')
]