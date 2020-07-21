from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
from broadcaster.sms import broadcast_sms
# from .tasks import send_parallel_sms
from .models import TempTeacher, TempStudent, TeacherProfile, StudentProfile
from django.contrib.auth.models import User


def create_or_update_user(instance):
    try:
        u = User.objects.get(username=str(int(instance.phone_number) * 30))
        u.first_name = instance.first_name
        u.last_name = instance.last_name
        u.email = instance.email
        u.set_password(instance.password)
        u.save()
    except:
        User.objects.create_user(username=str(int(instance.phone_number) * 30), password=instance.password,
                                 first_name=instance.first_name, last_name=instance.last_name,
                                 email=instance.email)


@receiver(pre_save, sender=TempTeacher)
def teacher_otp(sender, instance, **kwargs):
    # instance.otp = random.randrange(10101, 909090)
    instance.otp = "1234"
    content = "verification code is: " + str(instance.otp) + "\nthis code will valid for only 45 secs"
    # send_parallel_sms.delay(instance.phone_number, content)
    create_or_update_user(instance)
    broadcast_sms(instance.phone_number, content)


@receiver(pre_save, sender=TempStudent)
def student_otp(sender, instance, **kwargs):
    # instance.otp = random.randrange(10101, 909090)
    instance.otp = "1234"
    content = "verification code is: " + str(instance.otp) + "\nthis code will valid for only 45 secs"
    # send_parallel_sms.delay(instance.phone_number, content)
    create_or_update_user(instance)
    broadcast_sms(instance.phone_number, content)
