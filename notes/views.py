from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

def notes_list(request):
    notes = Note.objects.select_related('category').all()
    return render(request, 'notes/index.html', {'notes': notes})


