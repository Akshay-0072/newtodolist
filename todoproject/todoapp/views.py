from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect

def todoappView(request):
    return render(request, 'todolist.html')

def todoTable(request):
    return render(request, 'todotable.html')

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})

def addTodoView(request):
    x = request.POST['taskTitle', 'taskDesc']
    new_item = TodoListItem(taskTitle = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')