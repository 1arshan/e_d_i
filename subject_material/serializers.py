from rest_framework import serializers
from subject_material.models import VideoMaterial, Subject, StandardOrClass, NotesMaterial
#from user_login.serializers import NotesMaterialSerializer
from rest_framework_simplejwt import settings


class NotesMaterialSerializer2(serializers.ModelSerializer):
    class Meta:
        model = NotesMaterial
        fields = ['notes', 'question_ans', 'id']



class TeacherUploadSerializer(serializers.ModelSerializer):
    notes_material_link = NotesMaterialSerializer2(many=True)

    class Meta:
        model = VideoMaterial
        fields = ['subject_link', 'standard_link', 'topic', 'description', 'video_link',
                  'notes_material_link', 'chapter', 'thumbnail']

    def create(self, validated_data):
        notes_material_data = validated_data.pop('notes_material_link')
        temp = VideoMaterial.objects.create(**validated_data)
        for x in notes_material_data:
            NotesMaterial.objects.create(notes_link=temp, **x)
        return temp

    def update(self, instance, validated_data):
        notes_material_data = validated_data.pop('notes_material_link')
        data = instance.notes_material_link.all()
        data = list(data)

        instance.subject_link = validated_data.get('subject_link', instance.subject_link)
        instance.standard_link = validated_data.get('standard_link', instance.standard_link)
        instance.topic = validated_data.get('topic', instance.topic)
        instance.description = validated_data.get('description', instance.description)
        instance.video_link = validated_data.get('video_link', instance.video_link)
        instance.chapter = validated_data.get('chapter', instance.chapter)
        instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)

        instance.save()

        for x in notes_material_data:
            temp = data.pop(0)
            temp.notes_link = x.get('notes_link', temp.notes_link)
            temp.notes = x.get('notes', temp.notes)
            temp.question_ans = x.get('question_ans', temp.question_ans)
            temp.id = x.get('id', temp.id)
            temp.save()

        return instance
