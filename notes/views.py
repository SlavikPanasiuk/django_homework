from django.shortcuts import render
from django.http import HttpResponse




def notes_list(request):
    test_notes = [
        "Buy groceries",
        "Call Alice",
        "Read Django docs",
        "Walk the dog"
    ]
    return render(request, 'notes/index.html', {'notes': test_notes})


