from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Note, Noteitem, Notekey, Notetype, Status, Noteitemkey, PO, POItem, Product

def notes(request):
    notes = Note.objects.all()

    return render(request, 'note/notes.html', {'notes': notes})

def notescopy(request):
    notes = Note.objects.all()

    return render(request, 'note/notes-copy.html', {'notes': notes})

@require_http_methods(['POST'])
def add_note(request):
    note = None
    notetype = request.POST.get('notetype', '')
    notekey = request.POST.get('notekey', '')

    if notekey and notetype!=None:
        obj_notetype = Notetype.objects.get(notetype=notetype)
        obj_notekey, create_notekey = Notekey.objects.get_or_create(notekey=notekey)
        obj_po, create_po = PO.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=notetype)
        obj_note = Note.objects.get(id=obj_po.note_ptr_id)
    return render(request, 'note/partials/note.html', {'note': obj_note})

@require_http_methods(['GET', 'POST'])
def edit_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        note.notetype = request.POST.get('notetype', '')
        note.save()

        return render(request, 'note/partials/note.html', {'note': note})
    
    return render(request, 'note/partials/edit_note.html', {'note': note})

@require_http_methods(['PUT'])
def update_note(request, pk):

    note = Note.objects.get(id=pk)
    status = Status.objects.get(id=2)
    
    note.is_final = True
    note.status = status
    note.save()

    return render(request, 'note/partials/note.html', {'note': note})

@require_http_methods(['DELETE'])
def delete_note(request, pk):
    
    note = Note.objects.get(id=pk)
    
    note.delete()

    return HttpResponse()


def noteitems(request, noteref):
    notekey = Notekey.objects.get(notekey=noteref)
    #noteitem = Noteitem.objects.get(notekey_id=notekey.id)
    noteitems = Noteitem.objects.filter(notekey_id=notekey.id)
    note = Note.objects.filter(notekey_id=notekey)[:1].get()

    return render(request, 'note/noteitems.html', {'noteref': noteref, 'noteitems': noteitems, 'note': note})

@require_http_methods(['GET', 'POST'])
def edit_noteitem(request, pk, noteref):
    notekey = Notekey.objects.get(notekey=noteref)
    noteitem = Noteitem.objects.get(notekey_id=notekey.id, id=pk)

    if request.method == 'POST':
        product = request.POST.get('product', '')
        noteitem.product=Product.objects.get(product_name=product)
        noteitem.quantity = request.POST.get('quantity', '')
        noteitem.cost = request.POST.get('cost', '')
        noteitem.save()

        return render(request, 'note/partials/noteitem.html', {'noteref': noteref, 'noteitem': noteitem})
    
    return render(request, 'note/partials/edit_noteitem.html', {'noteref': noteref, 'noteitem': noteitem})

@require_http_methods(['POST'])
def add_noteitem(request, noteref):
    noteitem = None
    product = request.POST.get('product', '')
    quantity = request.POST.get('quantity', '')
    cost = request.POST.get('cost', '')

    if noteref:
        obj_note = Notekey.objects.get(notekey=noteref)
        obj_noteitemkey, create_noteitemkey = Noteitemkey.objects.get_or_create(notekey=obj_note, noteitemkey=obj_note.id)

        if product:
            obj_product = Product.objects.get(product_name=product)
            obj_poitem, create_poitem = POItem.objects.get_or_create(
                noteitemkey=obj_noteitemkey,
                notekey=obj_note,
                product=obj_product,
                quantity=quantity,
                cost=cost)
            
            noteitem = Noteitem.objects.get(id=obj_poitem.noteitem_ptr_id)
    
    return render(request, 'note/partials/noteitem.html', {'noteitem': obj_poitem, 'noteref': noteref})

@require_http_methods(['PUT'])
def update_noteitem(request, pk, noteref):

    notekey = Notekey.objects.get(notekey=noteref)
    noteitem = Noteitem.objects.get(notekey_id=notekey.id, id=pk)
    
    #noteitem = Noteitem.objects.get(pk=pk)
    noteitem.is_final = True
    noteitem.save()

    return render(request, 'note/partials/noteitem.html', {'noteitem': noteitem})

@require_http_methods(['DELETE'])
def delete_noteitem(request, pk, noteref):
    
    notekey = Notekey.objects.get(notekey=noteref)
    noteitem = Noteitem.objects.get(notekey_id=notekey.id, id=pk)
    
    #noteitem = Noteitem.objects.get(pk=pk)
    noteitem.delete()

    return HttpResponse()
