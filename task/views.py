# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.base import TemplateView  
from django.views.generic.edit import DeleteView
from task.forms import AddTaskForm, DeleteTaskForm
from task.models import Task

class SingleTaskView(TemplateView):
    template_name = "task/task.html"
    
    def __init__(self, task):
        super()
        self.task = task
    
    def get_context_data(self, **kwargs):
        context = {}
        context['id'] = self.task.id
        context['description'] = self.task.description
        context['done'] = self.task.done
        
class AllTasksView(TemplateView):
    template_name = "task/alltasks.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        context['tasks'] = [SingleTaskView(task) for task in Task.objects.all()]


class TaskView(TemplateView):
    template_name = "task/task_template.html"

    def get_context_data(self, **kwargs):
        context = {}
        form = AddTaskForm()
        context["form"] = form
        context["Tasks"] = Task.objects.all()
        context["formTaskList"] = DeleteTaskForm()
        return context

    def post(self, request):
        description = request.POST.get("description")
        Task.objects.create(description=description)
        return redirect("tasks")

class DeleteTaskView(View):
    def post(self, request):
        print request.POST
        tasks = request.POST.getlist("tasks")
        
        for t in tasks:
            Task.objects.get(description=t).delete()
        
        return redirect("tasks")
