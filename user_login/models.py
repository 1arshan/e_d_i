from django.db import models
from subject_material.models import VideoMaterial


class DoubtsQuestion(models.Model):
    material_link =models.ForeignKey(VideoMaterial,on_delete=models.CASCADE)
    doubts_question =models.TextField()

class DoubtsQuestionPhotos(models.Model):
    doubts_question_link =models.ForeignKey(DoubtsQuestion,on_delete=models.CASCADE)


