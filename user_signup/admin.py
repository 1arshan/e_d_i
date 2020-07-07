from django.contrib import admin
from .models import TempStudent, StudentProfile, TempTeacher, TeacherProfile


@admin.register(TempStudent)
class TempStudentAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "email", 'first_name', 'last_name')
    readonly_fields = ('date',)


@admin.register(TempTeacher)
class TempTeacherAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "email", 'first_name', 'last_name')
    readonly_fields = ('date',)

@admin.register(StudentProfile)
class StudentProfileInline(admin.ModelAdmin):
    list_display = ("phone_number", "email", 'first_name', 'last_name')


@admin.register(TeacherProfile)
class StudentProfileInline(admin.ModelAdmin):
    list_display = ("phone_number", "email", 'first_name', 'last_name')

