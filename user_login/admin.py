from .models import QuestionComment, DoubtsQuestionPhotos, \
    DoubtsQuestion,AnswerComment,DoubtsAnswer,DoubtsAnswerPhotos
from django.contrib import admin

#-----doubts qustion ----->>>>>>>
class CommentQuesInLine(admin.TabularInline):
    model = QuestionComment
    extra = 0


class QuesPhotosInLine(admin.TabularInline):
    model = DoubtsQuestionPhotos
    extra = 0


@admin.register(DoubtsQuestion)
class DoubtsQuestionAdmin(admin.ModelAdmin):
    list_display =('material_link','is_answered')
    list_filter = 'is_answered',
    inlines = [
        CommentQuesInLine, QuesPhotosInLine
    ]

##--------doubts answer ------->>>>>>>>
class CommentAnsInLine(admin.TabularInline):
    model = AnswerComment
    extra = 0


class PhotosInLine(admin.TabularInline):
    model = DoubtsAnswerPhotos
    extra = 0


@admin.register(DoubtsAnswer)
class DoubtsAnswerAdmin(admin.ModelAdmin):
    list_display =['answer_question_link']
    #list_filter = 'is_answered',
    inlines = [
        CommentAnsInLine, PhotosInLine
    ]
