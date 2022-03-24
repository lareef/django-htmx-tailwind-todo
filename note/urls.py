from django.urls import path

from note.views import notes, noteitems, add_note, update_note, delete_note, add_noteitem, update_noteitem, delete_noteitem, edit_noteitem

app_name = 'note'

urlpatterns = [
    path('', notes, name='notes'),
    path('add-note/', add_note, name='add_note'),
    path('update_note/<int:pk>/', update_note, name='update_note'),
    path('delete_note/<int:pk>/', delete_note, name='delete_note'),
    path('<int:noteref>/', noteitems, name='noteitems'),
    path('<int:noteref>/add-noteitem/', add_noteitem, name='add_noteitem'),
    path('<int:noteref>/update_noteitem/<int:pk>/', update_noteitem, name='update_noteitem'),
    path('<int:noteref>/delete_noteitem/<int:pk>/', delete_noteitem, name='delete_noteitem'),
    path('<int:noteref>/edit_noteitem/<int:pk>/', edit_noteitem, name='edit_noteitem'),
]