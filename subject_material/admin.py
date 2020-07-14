from django.contrib import admin
from .models import Subject, StandardOrClass, VideoMaterial, NotesMaterial
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


admin.site.register(StandardOrClass)

admin.site.register(NotesMaterial)


class NotesInLine(admin.TabularInline):
    model = NotesMaterial
    extra = 0


@admin.register(VideoMaterial)
class VideoMaterial(admin.ModelAdmin):
    list_display = ("subject_link", "standard_link", 'teacher_name', 'topic')
    inlines = [
        NotesInLine
    ]
