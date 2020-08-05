from rest_framework import serializers
from subject_material.models import VideoMaterial
from user_login.serializers import NotesMaterialSerializer
from rest_framework_simplejwt import settings
from drf_extra_fields.fields import Base64ImageField


class TeacherUploadSerializerGet(serializers.ModelSerializer):
    notes_material_link = NotesMaterialSerializer(many=True)

    # 'notes_material_link',
    class Meta:
        model = VideoMaterial
        fields = ['subject_link', 'standard_link', 'topic', 'description', 'video_link',
                  'chapter', 'thumbnail', 'id', 'notes_material_link']


"""
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
"""


class TeacherUploadSerializerPost(serializers.ModelSerializer):
    thumbnail = Base64ImageField()

    class Meta:
        model = VideoMaterial
        fields = ['subject_link', 'standard_link', 'topic', 'description', 'video_link',
                  'chapter', 'thumbnail', 'id']

    def create(self, validated_data):
        subject_link = validated_data.pop('subject_link')
        standard_link = validated_data.pop('standard_link')
        topic = validated_data.pop('topic')
        description = validated_data.pop('description')
        video_link = validated_data.pop('video_link')
        chapter = validated_data.pop('chapter')
        thumbnail = validated_data.pop('thumbnail')
        teacher_link = validated_data.pop('teacher_link')
        return VideoMaterial.objects.create(subject_link=subject_link, standard_link=standard_link, topic=topic,
                                            description=description, video_link=video_link, chapter=chapter,
                                            thumbnail=thumbnail,teacher_link=teacher_link)
