from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import PermissionDenied
from .models import Note


def notes_list_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    notes = Note.objects.filter(user__id=request.user.id)

    context = {
        'notes': notes
    }

    return render(request, 'notes/notes_list.html', context=context)


def notes_detail_view(request, pk=None):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    note = get_object_or_404(Note, id=pk, user__id=request.user.id)
    context = {
        'note': note,
    }

    return render(request, 'notes/notes_detail.html', context)
