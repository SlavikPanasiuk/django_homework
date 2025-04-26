from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

def notes_list(request):
    notes = Note.objects.select_related('category').all()
    return render(request, 'notes/index.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        if 'save' in request.POST:
            form = NoteForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                return redirect('note_detail', pk=note.pk)
        elif 'delete' in request.POST:
            note.delete()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_detail.html', {'form': form, 'note': note})