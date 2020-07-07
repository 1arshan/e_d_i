from rest_framework import serializers
from subject_material.models import VideoMaterial, Subject, StandardOrClass, NotesMaterial
from user_login.serializers import NotesMaterialSerializer


class TeacherUploadSerializer(serializers.ModelSerializer):
    #notes_material_link = NotesMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = VideoMaterial
        fields = ['subject_link', 'standard_link', 'topic', 'description', 'video_link']

    """def create(self, validated_data):
        notes_material_data = validated_data.pop('notes_material_link')
        temp = VideoMaterial.objects.create(**validated_data)
        for x in notes_material_data:
            NotesMaterial.objects.create(notes_link=temp, **x)
        return temp
"""