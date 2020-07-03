from django.contrib import admin
from .models import Subject, StandardOrClass, VideoMaterial, NotesMaterial

admin.site.register(Subject)
admin.site.register(StandardOrClass)


class NotesInLine(admin.TabularInline):
    model = NotesMaterial
    extra = 0


@admin.register(VideoMaterial)
class VideoMaterial(admin.ModelAdmin):
    list_display = ("subject_link", "standard_link")
    inlines = [
        NotesInLine
    ]
