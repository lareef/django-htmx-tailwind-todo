from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Note, Noteitem, Notekey, Notetype, Status, Noteitemkey, PO, POItem, Product, SO, SOItem

# def notes(request, pk=""):
#     notetype = Notetype.objects.all()
#     notes = None
#     if pk:
#         notes = Note.objects.filter(notetype=pk)
#         return render(request, 'note/notes.html', {'notes': notes})
#     return render(request, 'note/notes.html', {'notes': notes})

def notes(request):
    notetypes = Notetype.objects.all()
    #pk = request.POST.get('notetype', '')
    notes = None
    if request.method == 'GET':
        notetype = request.GET.get('notetype', '')
        if notetype:
            notes = Note.objects.filter(notetype_id=notetype)
        return render(request, 'note/notes-copy.html', {'notes': notes, 'notetypes': notetypes})
    return render(request, 'note/notes.html', {'notes': notes, 'notetypes': notetypes})

def init(request):
    notetypes = Notetype.objects.all()
    #pk = request.POST.get('notetype', '')
    notes = None
    return render(request, 'note/notes.html', {'notes': notes, 'notetypes': notetypes})

@require_http_methods(['POST'])
def add_note(request):
    note = None
    notetype = request.POST.get('notetype', '')
    notekey = request.POST.get('notekey', '')

    if notekey and notetype!=None:
        obj_notetype = Notetype.objects.get(id=notetype)
        obj_notekey, create_notekey = Notekey.objects.get_or_create(notekey=notekey)

        
        if obj_notetype.id == 1:
            obj_po, create_po = PO.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=obj_notetype.id)
            obj_note = Note.objects.get(id=obj_po.note_ptr_id)

        if obj_notetype.id == 2:
            obj_so, create_so = SO.objects.get_or_create(notekey=obj_notekey, notetype=obj_notetype, typ=obj_notetype.id)
            obj_note = Note.objects.get(id=obj_so.note_ptr_id)
        
        #obj_notekey, create_notekey = Notekey.objects.get_or_update(notekey=obj_notekey, notetype=obj_notetype)

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


def noteitems(request, pk):
    #notekey = Notekey.objects.get(notekey=noteref)
    note = Note.objects.get(id=pk)
    noteref = note.notekey_id
    noteitems = Noteitem.objects.filter(notekey_id=noteref, notetypekey_id=note.notetype_id)
    #note = Note.objects.filter(notekey_id=notekey)[:1].get()

    return render(request, 'note/noteitems.html', {'noteref': noteref, 'noteitems': noteitems, 'note': note})

@require_http_methods(['GET', 'POST'])
def edit_noteitem(request, pk):
    #notekey = Notekey.objects.get(notekey=note)
    #obj_notetype = Notetype.objects.get(id=note.notetype)
    noteitem = Noteitem.objects.get(id=pk)

    if request.method == 'POST':
        product = request.POST.get('product', '')
        noteitem.product=Product.objects.get(product_name=product)
        noteitem.quantity = request.POST.get('quantity', '')
        noteitem.cost = request.POST.get('cost', '')
        noteitem.weight = request.POST.get('weight', '')
        noteitem.save()
        
        #note = Note.objects.filter(notekey_id=notekey)[:1].get()

        return render(request, 'note/partials/noteitem.html', {'noteitem': noteitem})
    
    return render(request, 'note/partials/edit_noteitem.html', {'noteitem': noteitem})

@require_http_methods(['POST'])
def add_noteitem(request, note):
    noteitem = None
    product = request.POST.get('product', '')
    quantity = request.POST.get('quantity', '')
    cost = request.POST.get('cost', '')
    weight = request.POST.get('weight', '')

    if note:
        note = Note.objects.get(id=note)
        obj_notekey = Notekey.objects.get(id=note.notekey_id)
        obj_notetype = Notetype.objects.get(id=note.notetype_id)
        obj_noteitemkey, create_noteitemkey = Noteitemkey.objects.get_or_create(notekey=obj_notekey)
        if product:
            obj_product = Product.objects.get(product_name=product)
            if note.notetype_id == 1:
                obj_item, create_poitem = POItem.objects.get_or_create(
                    noteitemkey=obj_noteitemkey,
                    notekey=obj_notekey,
                    notetypekey=obj_notetype,
                    product=obj_product,
                    quantity=quantity,
                    weight=weight,
                    cost=cost)
            if note.notetype_id == 2:
                obj_item, create_poitem = SOItem.objects.get_or_create(
                    noteitemkey=obj_noteitemkey,
                    notekey=obj_notekey,
                    product=obj_product,
                    notetypekey=obj_notetype,
                    quantity=quantity,
                    weight=weight,
                    cost=cost)
                               
            #noteitem = Noteitem.objects.get(id=obj_poitem.noteitem_ptr_id)
    
    return render(request, 'note/partials/noteitem.html', {'noteitem': obj_item, 'note': note})

@require_http_methods(['PUT'])
def update_noteitem(request, pk):

    # notekey = Notekey.objects.get(notekey=noteref)
    noteitem = Noteitem.objects.get(id=pk)
    
    #noteitem = Noteitem.objects.get(pk=pk)
    noteitem.is_final = True
    noteitem.save()

    return render(request, 'note/partials/noteitem.html', {'noteitem': noteitem})

@require_http_methods(['DELETE'])
def delete_noteitem(request, pk):
    
    #notekey = Notekey.objects.get(notekey=noteref)
    noteitem = Noteitem.objects.get(id=pk)
    
    #noteitem = Noteitem.objects.get(pk=pk)
    noteitem.delete()

    return HttpResponse()
