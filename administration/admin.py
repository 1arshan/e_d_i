from django.contrib import admin
from .models import TeacherVerification, VideoMaterialVerification, CrashReport, InstituteVerification


@admin.register(TeacherVerification)
class TeacherProfileInline(admin.ModelAdmin):
    list_display = ("phone_number", "email", 'first_name', 'last_name', 'is_verified')

    def get_queryset(self, request):
        queryset = TeacherVerification.objects.filter(is_verified=False)
        return queryset


@admin.register(VideoMaterialVerification)
class VideoMaterialInline(admin.ModelAdmin):
    list_display = ("subject_link", "standard_link", 'teacher_name', 'chapter', 'is_verified')

    def get_queryset(self, request):
        queryset = VideoMaterialVerification.objects.filter(is_verified=False)
        return queryset


@admin.register(InstituteVerification)
class InstituteInline(admin.ModelAdmin):
    list_display = ("name", "pincode", 'is_verified')

    def get_queryset(self, request):
        queryset = InstituteVerification.objects.filter(is_verified=False)
        return queryset


@admin.register(CrashReport)
class CrashReportAdmin(admin.ModelAdmin):
    list_display = ("app_version_code", "app_version_name", 'andriod_version', 'package_name')
