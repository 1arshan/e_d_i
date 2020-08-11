from .models import Institute
from django.db.models.signals import pre_save
from django.dispatch import receiver

"""
@receiver(pre_save, sender=Institute)
def add_teacher_name(sender, instance, **kwargs):
    instance.admin_name = instance.admin_link.first_name + " " + instance.admin_link.last_name

"""