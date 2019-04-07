from django.shortcuts import render, redirect

from todos.forms import TodoForm
from .models import Todo


def show(request):
    todos = Todo.objects.order_by('status', '-created_date')
    return render(request,"show.html",{'todos':todos})

def index(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm()
        
    return render(request,'index.html',{'form':form})


def edit(request, id):
    todo = Todo.objects.get(id=id)
    return render(request,'edit.html', {'todo':todo})


def update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST, instance = todo)
    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, 'edit.html', {'employee': todo})


def destroy(request, id):
    employee = Todo.objects.get(id=id)
    employee.delete()
    return redirect("/")