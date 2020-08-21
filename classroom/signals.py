from .models import InstituteTeacher, Class, AssignmentSubmission, StudentAttach

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


@receiver(pre_save, sender=InstituteTeacher)
def institute_teacher_signal(sender, instance, **kwargs):
    instance.teacher_name = instance.teacher_link.first_name + " " + instance.teacher_link.last_name


@receiver(pre_save, sender=Class)
def class_signal(sender, instance, **kwargs):
    instance.teacher_name = instance.teacher_link.first_name + " " + instance.teacher_link.last_name


@receiver(pre_save, sender=AssignmentSubmission)
def assgn_submission_signal(sender, instance, **kwargs):
    instance.student_name = instance.student_link.first_name + " " + instance.student_link.last_name


@receiver(pre_save, sender=StudentAttach)
def student_class_signal(sender, instance, **kwargs):
    instance.student_name = instance.student_link.first_name + " " + instance.student_link.last_name
