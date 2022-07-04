from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addtodoitem/',views.addtodoitem,name='addtodoitem'),
    path('deleteitem/<int:id>',views.deleteitem,name='deleteitem'),
    path('todoitem-list/<int:id>',views.todoitemlist,name='todoitem-list'),
    path('deletelistitem/<int:id>/<int:t_id>',views.deletelistitem,name='deletelistitem'),
    path('addmoreitems/<int:id>',views.addmoreitems,name='addmoreitems'),
    path('addlistitem/<int:id>',views.addlistitem,name='addlistitem'),
    
]