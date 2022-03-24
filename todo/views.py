from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Todo, Doc, Master

def todos(request):
    todos = Todo.objects.all()

    return render(request, 'todo/todos.html', {'todos': todos})

@require_http_methods(['GET', 'POST'])
def edit_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        todo.title = request.POST.get('title', '')
        todo.save()

        return render(request, 'todo/partials/todo.html', {'todo': todo})
    
    return render(request, 'todo/partials/edit.html', {'todo': todo})

@require_http_methods(['POST'])
def add_todo(request):
    todo = None
    title = request.POST.get('title', '')

    if title:
        todo = Todo.objects.create(title=title)
    
    return render(request, 'todo/partials/todo.html', {'todo': todo})

@require_http_methods(['PUT'])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = True
    todo.save()

    return render(request, 'todo/partials/todo.html', {'todo': todo})

@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return HttpResponse()

# -----------------------------------------------------------------

def masters(request):
    masters = Master.objects.all()

    return render(request, 'doc/masters.html', {'masters': masters})

def masterscopy(request):
    masters = Master.objects.all()

    return render(request, 'doc/masters-copy.html', {'masters': masters})

@require_http_methods(['POST'])
def add_master(request):
    master = None
    master = request.POST.get('master', '')

    if master:
        obj_master, create_master = Master.objects.get_or_create(mname=master)

    return render(request, 'doc/partials/master.html', {'master': obj_master})

@require_http_methods(['GET', 'POST'])
def edit_master(request, pk):
    master = Master.objects.get(pk=pk)

    if request.method == 'POST':
        master.mname = request.POST.get('mname', '')
        master.save()

        return render(request, 'doc/partials/master.html', {'master': master})
    
    return render(request, 'doc/partials/edit_master.html', {'master': master})

def docs(request, master):
    docs = Doc.objects.filter(master=master)

    return render(request, 'doc/docs.html', {'master': master, 'docs': docs})

@require_http_methods(['GET', 'POST'])
def edit_doc(request, pk, master):
    doc = Doc.objects.get(pk=pk)

    if request.method == 'POST':
        doc.title = request.POST.get('title', '')
        doc.save()

        return render(request, 'doc/partials/doc.html', {'doc': doc})
    
    return render(request, 'doc/partials/edit_doc.html', {'doc': doc})

@require_http_methods(['POST'])
def add_doc(request, master):
    doc = None
    title = request.POST.get('title', '')

    if master:
        obj_master, create_master = Master.objects.get_or_create(mname=master)

        if title:
            doc = Doc.objects.create(title=title, master=obj_master)
    
    return render(request, 'doc/partials/doc.html', {'doc': doc, 'master': master})

@require_http_methods(['PUT'])
def update_doc(request, pk, master):
    doc = Doc.objects.get(pk=pk)
    doc.is_done = True
    doc.save()

    return render(request, 'doc/partials/doc.html', {'doc': doc})

@require_http_methods(['DELETE'])
def delete_doc(request, pk, master):
    doc = Doc.objects.get(pk=pk)
    doc.delete()

    return HttpResponse()