from .models import VideoMaterial,NotesMaterial
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=VideoMaterial)
def add_teacher_name(sender, instance, **kwargs):
    instance.teacher_name =instance.teacher_link.first_name + " " + instance.teacher_link.last_name

@receiver(pre_save, sender=NotesMaterial)
def change_file_path(sender, instance, **kwargs):
    print(instance.pk)