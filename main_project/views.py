from django.shortcuts import render,redirect
from task.models import task_model

def home(request):
    return render(request,"./home.html")

def show_task(request):
    show_task_model = task_model.objects.all()
    return render(request,"./show_task.html",{'show_task_model':show_task_model})


