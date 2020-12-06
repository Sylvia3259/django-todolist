from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    forms = TaskForm()
    return render(request, 'todolist/index.html', { 'tasks': tasks, 'forms': forms })


def create(request):
    form = TaskForm(request.POST)
    form.save()
    return HttpResponseRedirect(reverse('index'))


def complete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = not task.completed
    task.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('index'))
