from django.contrib import admin
from django.urls import path, include

from todo.views import todos, add_todo, update_todo, delete_todo, edit_todo, docs, add_doc, update_doc, delete_doc, edit_doc, masters, add_master, masterscopy 

urlpatterns = [
    path('', todos, name='todos'),
    path('add-todo/', add_todo, name='add_todo'),
    path('update/<int:pk>/', update_todo, name='update_todo'),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),
    path('edit/<int:pk>/', edit_todo, name='edit_todo'),

    path('doc/', masters, name='masters'),
    path('docs/', masterscopy, name='masterscopy'),
    path('add-master/', add_master, name='add_master'),
    # path('master/update_master/<int:pk>/', update_master, name='update_master'),
    # path('master/delete_master/<int:pk>/', delete_master, name='delete_master'),
    # path('master/edit_master/<int:pk>/', edit_master, name='edit_master'),
    
    path('doc/<int:master>/', docs, name='docs'),
    path('doc/<int:master>/add-doc/', add_doc, name='add_doc'),
    path('doc/<int:master>/update_doc/<int:pk>/', update_doc, name='update_doc'),
    path('doc/<int:master>/delete_doc/<int:pk>/', delete_doc, name='delete_doc'),
    path('doc/<int:master>/edit_doc/<int:pk>/', edit_doc, name='edit_doc'),
    
    path('admin/', admin.site.urls),
    path('note/', include('note.urls')),
]
