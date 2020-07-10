from .models import QuestionComment, DoubtsQuestionPhotos, DoubtsQuestion
from django.contrib import admin


class CommentInLine(admin.TabularInline):
    model = QuestionComment
    extra = 0


class PhotosInLine(admin.TabularInline):
    model = DoubtsQuestionPhotos
    extra = 0


@admin.register(DoubtsQuestion)
class VideoMaterial(admin.ModelAdmin):
    list_display =('material_link','is_answered')
    inlines = [
        CommentInLine, PhotosInLine
    ]
