from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from .models import Task
# Create your views here.

def taskList(request):
    tasks = Task.objects.all()
    
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})
    

def taskDetail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'todoapp/task_detail.html', {'task': task})


def taskCreate(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        task = Task.objects.create(
            title = title,
            description = description,
            creation_time = timezone.now(),
            completion_time = due_date

        )

        task.save()

        return redirect('tasks')

    return render(request, 'todoapp/task_create.html', {})
    

