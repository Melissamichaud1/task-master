from django.shortcuts import render, redirect

from tasks.models import Task
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def show_task(request):
    task = Task.objects.filter(assignee=request.user)
    context = {
        "task_object": task,
    }
    return render(request, "tasks/list.html", context)
