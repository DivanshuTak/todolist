from django.shortcuts import render, redirect
from django.http import HttpResponse 
from todos.models import Todo


def index(request):
    todos = Todo.objects.all()[:10]
    context = {
            'todos':todos
        }
    return render(request, 'index.djhtml', context)

def details(request, id):
    todo = Todo.objects.get(id = id)
    context = {
            'todo':todo
        }
    return render(request, 'details.djhtml', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        created_at = request.POST['created_at']
        
        todo =  Todo(title=title, text=text , created_at=created_at)
        todo.save()
        
        return redirect('/todos')
    else:
        return render(request,'add.djhtml')
