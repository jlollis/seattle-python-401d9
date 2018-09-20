from django.contrib import admin
from .models import Note

# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_modified')


admin.site.register(Note, NoteAdmin)