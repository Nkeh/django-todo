from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
# Create your views here.

def taskList(request):
    tasks = Task.objects.all()
    
    return render(request, 'todoapp/task-list.html', {'tasks': tasks})
    

def taskDetail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'todoapp/task-detail.html', {'task': task})
