from django.db import models
from datetime import datetime,date
from django.utils import timezone


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.TextField(max_length=200,unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='1. TO DO LIST'

class ToDoListItems(models.Model):
    content = models.TextField(max_length=200,unique=True)
    description = models.TextField(null=True, blank=True)
    todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    due_date = models.DateField(default=one_week_hence,null=True,blank=True)
    checked = models.BooleanField(default=False)
    
    def __str__(self):
        return self.content
    

    class Meta:
        verbose_name_plural='2. TO DO LIST ITEMS'

