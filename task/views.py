from django.shortcuts import render,redirect
from task.forms import task_form
from task.models import task_model

# Create your views here.
def add_task(request):
    if request.method == "POST":
        add_task_form = task_form(request.POST)
        if add_task_form.is_valid():
            add_task_form.save()
            return redirect("show_task")
       
    else : 
        add_task_form = task_form()
       
    
    return render(request,"./task_form.html",{'add_task_form':add_task_form})

# editing task 

def edit_task(request,id):
    task = task_model.objects.get(pk=id)
    add_task_form = task_form(instance = task)

    if request.method == "POST":
        add_task_form = task_form(request.POST,instance = task)
        if add_task_form.is_valid():
            add_task_form.save()
            return redirect("show_task")
    return render(request,"./task_form.html",{'add_task_form':add_task_form})

def delete_task(request,id):
    task = task_model.objects.get(pk=id)
    task.delete()
    return redirect("show_task")
    
