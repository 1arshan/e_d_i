from django.contrib import admin
from .models import Institute, InstituteTeacher, Class, Assignment, StudentAttach,AssignmentSubmission ,\
   QuestionBank,StudentTest,StudentTestData,ClassTest,ClassTestQuestion
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ("name", "pincode", 'is_verified','pk')
    readonly_fields = ('pk',)


@admin.register(InstituteTeacher)
class InstituteTeacherAdmin(admin.ModelAdmin):
    list_display = ("teacher_link", "institute_link", 'administrative_right')


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("code", "standard_or_class", 'name', 'teacher_link', 'institute_link', 'pk')
    readonly_fields = ('pk',)


@admin.register(Assignment)
class AssingmentAdmin(admin.ModelAdmin):
    list_display = ("class_link", "pk")
    readonly_fields = ('pk',)


@admin.register(StudentAttach)
class StudentAttachAdmin(admin.ModelAdmin):
    list_display = ("class_link", 'student_link', "pk")
    readonly_fields = ('pk',)


@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ("assignment_link", 'time_remark','student_link', "pk")
    readonly_fields = ('pk','submission_datetime')


@admin.register(QuestionBank)
class QuestionBankAdmin(admin.ModelAdmin,DynamicArrayMixin):
    list_display = ('class_link','subject_link','created_by','chapter', "pk")
    readonly_fields = ('pk',)


class StudentTestDataInLine(admin.TabularInline):
    model = StudentTestData
    extra = 0


@admin.register(StudentTest)
class StudentTestAdmin(admin.ModelAdmin):
    list_display = ("type", "student_link", 'total_mark', 'mark_score')
    inlines = [
        StudentTestDataInLine
    ]


class ClassTestQuestionInLine(admin.TabularInline):
    model = ClassTestQuestion
    extra = 0


@admin.register(ClassTest)
class ClassTestAdmin(admin.ModelAdmin):
    list_display = ("class_link", "mark_per_ques", 'negative_marking')
    inlines = [
        ClassTestQuestionInLine
    ]

