from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
from broadcaster.sms import broadcast_sms
# from .tasks import send_parallel_sms
from .models import TempTeacher, TempStudent, TeacherProfile, StudentProfile
from django.contrib.auth.models import User


@receiver(pre_save, sender=TempTeacher)
def teacher_otp(sender, instance, **kwargs):
    # instance.otp = random.randrange(10101, 909090)
    instance.otp = "1234"
    content = "verification code is: " + str(instance.otp) + "\nthis code will valid for only 45 secs"
    # send_parallel_sms.delay(instance.phone_number, content)
    try:

        User.objects.update_or_create(username=str(int(instance.phone_number) * 30),
                                      defaults={

                                          "email": instance.email,
                                          "first_name": instance.first_name,
                                          "last_name": instance.last_name
                                      })  # .set_password(instance.password)
        u = User.objects.get(username=str(int(instance.phone_number) * 30))
        u.set_password(instance.password)
        u.save()
        instance.password = "***************"
    except:
        pass
    broadcast_sms(instance.phone_number, content)


@receiver(pre_save, sender=TempStudent)
def student_otp(sender, instance, **kwargs):
    # instance.otp = random.randrange(10101, 909090)
    instance.otp = "1234"
    content = "verification code is: " + str(instance.otp) + "\nthis code will valid for only 45 secs"
    # send_parallel_sms.delay(instance.phone_number, content)
    try:
        User.objects.update_or_create(username=str(int(instance.phone_number) * 30),
                                          defaults={
                                              "password": instance.password,
                                              "email": instance.email,
                                              "first_name": instance.first_name,
                                              "last_name": instance.last_name
                                          })
        u = User.objects.get(username=str(int(instance.phone_number) * 30))
        u.set_password(instance.password)
        u.save()
        instance.password = "***************"
    except:
        pass
    broadcast_sms(instance.phone_number, content)
