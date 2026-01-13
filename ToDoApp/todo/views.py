from django.shortcuts import render,redirect
from django.views import View
from todo.forms import TodoForm
from todo.models import TodoModel
from django.contrib import messages
# Create your views here.


class UserHomeView(View):
    def get(self,request):
        return render(request,'userHome.html')
    
class AddTodoView(View):
    def get(self,request):
        form=TodoForm()
        return render(request,'addtodo.html',{"form":form})
    def post(self,request):
        form_data=TodoForm(data=request.POST)
        userobj=request.user
        print(userobj)
        if form_data.is_valid():
            todo=form_data.save(commit=False)
            todo.user=userobj
            todo.save()
            messages.info(request,"Todo Succesuflly added")
            return redirect('uhome')
        messages.warning(request,"Invalid Input recieved")
        return render(request,'addtodo.html',{'form':form_data})

class TodoListView(View):
    def get(self,request):
        todoqs=TodoModel.objects.filter(user=request.user)
        return render(request,"todolist.html",{"data":todoqs})

class TodoDeleteView(View):
    def get(self,request,**kwargs):
        tdid=kwargs.get('tdid')
        qo=TodoModel.objects.get(id=tdid)
        qo.delete()
        messages.success(request,"Todo removed Succesfully")
        return redirect('tdlist')
    
# class StatusUpdateView(View):
#     def get(self,request,**kwargs):
#         tdid=kwargs.get('tdid')
#         qo=TodoModel.objects.get(id=tdid)
#         qo.status="Completed"
#         qo.save()
#         return redirect('tdlist')
    
# class TodoCancelView(View):
#     def get(self,request,**kwargs):
#         tdid=kwargs.get('tdid')
#         qo=TodoModel.objects.get(id=tdid)
#         qo.status="Cancelled"
#         qo.save()
#         return redirect('tdlist')

class StatusUpdateView(View):
    def get(self,request,**kwargs):
        tdid=kwargs.get('tdid')
        todo=TodoModel.objects.get(id=tdid)
        status=kwargs.get('status')
        todo.status=status
        todo.save()
        return redirect('tdlist')
    
class EditTodoView(View):
    def get(self,request,**kwargs):
        tdid=kwargs.get('tdid')
        qo=TodoModel.objects.get(id=tdid)
        form=TodoForm(instance=qo)
        return render(request,'edittodo.html',{'form':form})
    def post(self,request,**kwargs):
        tdid=kwargs.get('tdid')
        print(tdid)
        todo=TodoModel.objects.get(id=tdid)
        form_data=TodoForm(data=request.POST,instance=todo)
        if form_data.is_valid():
            form_data.save()
            messages.info(request,"Todo Successfully edited")
            return redirect('tdlist')
        messages.warning(request,"Invalid input recieved")
        return render(request,'edittodo.html',{'form':form_data})

