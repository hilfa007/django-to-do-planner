from email import message
from django.shortcuts import redirect, render,HttpResponseRedirect
from . models import*
from django.urls import reverse
from django.db import IntegrityError
from django.utils.timezone import datetime #important if using timezones

def index(request):
    today = datetime.today()
    all_lists = ToDoList.objects.all()
    all_items = ToDoListItems.objects.all()
    return render(request,'todo.html',{'all_lists' : all_lists,'all_items':all_items,'today':today})
    
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
    today = datetime.today()
    todolist = ToDoList.objects.get(id=id)
    all = ToDoListItems.objects.filter(todolist=todolist).order_by('-id')
    return render(request,'todo_item_list.html',{'todolist' : todolist,'all':all,'today':today})

def deletelistitem(request,id,t_id):
    id = ToDoListItems.objects.get(id=id)
    id.delete()
    todolist = ToDoList.objects.get(id=t_id)
    all = ToDoListItems.objects.filter(todolist=todolist).order_by('-id')
    return render(request,'todo_item_list.html',{'todolist' : todolist,'all':all})

def addlistitem(request,id):
    todolist = ToDoList.objects.get(id=id)
    title = request.POST['title']
    desc = request.POST['desc']
    date = request.POST['date']
    plan = ToDoListItems(content=title,description=desc,todolist=todolist,due_date=date)
    all = ToDoListItems.objects.filter(todolist=todolist).order_by('-id')
    try:
        plan.save()
    except IntegrityError as err:
        return HttpResponseRedirect('/')
    return render(request,'todo_item_list.html',{'todolist' : todolist,'all':all})

