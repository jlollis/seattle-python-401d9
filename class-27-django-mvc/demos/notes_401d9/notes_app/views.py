from django.shortcuts import render, get_object_or_404
from .models import Note


def notes_list_view(request):
    notes = Note.objects.all()

    context = {
        'notes': notes
    }

    return render(request, 'notes/notes_list.html', context=context)


def notes_detail_view(request, pk=None):
    note = get_object_or_404(Note, id=pk)
    context = {
        'note': note,
    }

    return render(request, 'notes/notes_detail.html', context)
