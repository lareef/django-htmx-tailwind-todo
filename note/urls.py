from django.urls import path

from note.views import init, notes, noteitems, add_note, update_note, delete_note, add_noteitem, update_noteitem, delete_noteitem, edit_noteitem

app_name = 'note'

urlpatterns = [
    path('', init, name='init'),
    path('notes/', notes, name='notes'),
    #path('init/', notes, name='init'),
    path('add-note/', add_note, name='add_note'),
    path('update_note/<int:pk>/', update_note, name='update_note'),
    path('delete_note/<int:pk>/', delete_note, name='delete_note'),
    path('noteitems/<int:pk>/', noteitems, name='noteitems'),
    path('<int:note>/add-noteitem/', add_noteitem, name='add_noteitem'),
    path('update_noteitem/<int:pk>/', update_noteitem, name='update_noteitem'),
    path('delete_noteitem/<int:pk>/', delete_noteitem, name='delete_noteitem'),
    path('edit_noteitem/<int:pk>/', edit_noteitem, name='edit_noteitem'),
]