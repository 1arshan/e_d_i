from rest_framework import serializers
from subject_material.models import VideoMaterial, Subject, StandardOrClass, NotesMaterial


class NotesMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesMaterial
        fields = ['notes', 'question_ans']


class StudentHomePageSerializer(serializers.ModelSerializer):
    notes_material_link = NotesMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = VideoMaterial
        fields = ['subject_link', 'standard_link', 'topic', 'description', 'video_link', 'teacher_link',
                  'notes_material_link']
