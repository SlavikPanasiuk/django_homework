from django.urls import path

from . import views

urlpatterns =[
    path('', views.notes_list, name='notes_list'),
    path('notes/create/', views.create_note, name='create_note'),
    path('notes/<int:pk>/', views.note_detail, name='note_detail'),
]