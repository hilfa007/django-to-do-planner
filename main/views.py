from email import message
from django.shortcuts import redirect, render,HttpResponseRedirect
from . models import*
from django.urls import reverse
from django.db import IntegrityError

def index(request):
    all_items = ToDoList.objects.all()
    return render(request,'todo.html',{'all_items' : all_items})
    
def addtodoitem(request):
    x = request.POST['content']
    if x != '':
        content_item = ToDoList(title = x)
        try:
            content_item.save()
        except IntegrityError as err:
           return HttpResponseRedirect('/') 
    return HttpResponseRedirect('/')

def deleteitem(request,id):
    id = ToDoList.objects.get(id=id)
    id.delete()
    return HttpResponseRedirect(reverse('index'))


def todoitemlist(request,id):
    todolist = ToDoList.objects.get(id=id)
    all = ToDoListItems.objects.all().order_by('-id')
    return render(request,'todo_item_list.html',{'todolist_id' : todolist,'all':all})

def addlistitem(request,id):
    todolist_id = ToDoList.objects.get(id=id)
    title = request.POST['title']
    desc = request.POST['desc']
    plan = ToDoListItems(content=title,description=desc,todolist=todolist_id)
    all = ToDoListItems.objects.all().order_by('-id')
    try:
        plan.save()
    except IntegrityError as err:
        return HttpResponseRedirect('/')
    plan.save()
    return render(request,'todo_item_list.html',{'todolist_id' : todolist_id,'all':all})