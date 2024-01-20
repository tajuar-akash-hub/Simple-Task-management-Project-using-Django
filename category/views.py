from django.shortcuts import render,redirect
from . forms import category_form

# Create your views here.
def add_category(request):
    if request.method == "POST":
        add_catagory_form = category_form(request.POST)
        if add_catagory_form.is_valid():
            add_catagory_form.save()
            return redirect("add_category")
    else : 
        add_catagory_form = category_form()
        

    return render(request,"./catagory_form.html",{'add_catagory_form':add_catagory_form})



    



    
