from django.contrib import admin
from .models import Institute, InstituteTeacher,Class


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ("name", "pincode", 'is_verified')
    readonly_fields = ('pk',)


@admin.register(InstituteTeacher)
class InstituteTeacherAdmin(admin.ModelAdmin):
    list_display = ("teacher_link", "institute_link", 'administrative_right')


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("code", "standard_or_class",'subject', 'teacher_link','institute_link')
