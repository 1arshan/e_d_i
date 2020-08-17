from django.contrib import admin
from .models import Institute, InstituteTeacher, Class, Assignment, StudentAttach,AssignmentSubmission


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ("name", "pincode", 'is_verified')
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
