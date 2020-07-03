from django.contrib import admin
from .models import TempStudent, StudentProfile, TempTeacher, TeacherProfile


admin.site.register(TempStudent)
admin.site.register(StudentProfile)
admin.site.register(TempTeacher)
admin.site.register(TeacherProfile)
"""
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
"""
"""
@admin.register(Student)
class UserProxyAdmin(admin.ModelAdmin):
    fields = ['username', 'first_name', 'last_name', 'email']
    list_display = ['username', 'first_name', 'last_name', 'email']
    inlines = [
        StudentProfileInline,
    ]
"""