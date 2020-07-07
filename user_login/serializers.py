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
        fields = ['subject_link', 'standard_link', 'topic', 'description', 'video_link',
                  'notes_material_link', 'teacher_name','teacher_link']

    def create(self, validated_data):
        notes_material_data = validated_data.pop('notes_material_link')
        temp = VideoMaterial.objects.create(**validated_data)
        for x in notes_material_data:
            NotesMaterial.objects.create(notes_link=temp, **x)
        return temp


"""class FormInfoSerializers(serializers.ModelSerializer):
    single_ans_ques = SingleAnsQuesSerializer(many=True, read_only=True)
    class Meta:
        model = FormInfo
        fields = ['id', 'username_email', 'headline', 'summary',
                  'single_ans_ques', 'multi_ans_ques', 'file_ques', 'checkbox_ques_ans',
                  'linear_scale_ans']
    def create(self, validated_data):
        single_ans_data = validated_data.pop('single_ans_ques')
        temp = FormInfo.objects.create(**validated_data)
        for x in single_ans_data:
            SingleAnsQues.objects.create(single_ans_ques_link=temp, **x)

        return temp
"""
