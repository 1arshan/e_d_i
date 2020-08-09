from django.contrib import admin
from .models import Institute, InstituteTeacher


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ("name", "pincode", 'admin_name', 'is_verified')


@admin.register(InstituteTeacher)
class InstituteTeacherAdmin(admin.ModelAdmin):
    list_display = ("teacher_link", "institute_link", 'administrative_right')
