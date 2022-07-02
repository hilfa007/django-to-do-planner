from django.contrib import admin
from .models import ToDoList, ToDoListItems

# ToDoList
class ToDoListAdmin(admin.ModelAdmin):
    list_display=('id','title')
admin.site.register(ToDoList,ToDoListAdmin)
# ToDoListItem
class ToDoListItemsAdmin(admin.ModelAdmin):
    list_display=('id','content','description','todolist')
admin.site.register(ToDoListItems,ToDoListItemsAdmin)
