from rest_framework import serializers
from .models import CrashReport

class CrashReportSerializers(serializers.ModelSerializer):
    class Meta:
        model=CrashReport
        fields =['app_version_code','app_version_name','andriod_version','package_name','build','stack_trace']