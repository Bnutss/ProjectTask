from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.order_by('deadline', '-priority')
    completed_tasks = Task.objects.filter(status='completed').order_by('-priority')
    return render(request, 'tracker/task_list.html', {'tasks': tasks, 'completed_tasks': completed_tasks})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tracker/create_task.html', {'form': form})


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tracker/edit_task.html', {'form': form, 'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tracker/delete_task.html', {'task': task})


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = 'completed'
    task.save()
    return redirect('task_list')
