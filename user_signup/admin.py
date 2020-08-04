from django.contrib import admin
from .models import TempStudent, StudentProfile, TempTeacher, TeacherProfile, TestingModel
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


@admin.register(TempStudent)
class TempStudentAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "email", 'first_name', 'last_name')
    readonly_fields = ('date',)


@admin.register(TempTeacher)
class TempTeacherAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "email", 'first_name', 'last_name')
    exclude = ['password']
    readonly_fields = ('date',)


@admin.register(StudentProfile)
class StudentProfileInline(admin.ModelAdmin):
    list_display = ("phone_number", "email", 'first_name', 'last_name', 'standard_or_class')
    readonly_fields = ('date',)


@admin.register(TeacherProfile)
class TeacherProfileInline(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ("phone_number", "email", 'first_name', 'last_name')



@admin.register(TestingModel)
class TeacherProfileInline(admin.ModelAdmin, DynamicArrayMixin):
    readonly_fields=('id',)
