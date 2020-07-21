# Generated by Django 3.0.8 on 2020-07-19 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_signup', '0002_auto_20200715_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='tempstudent',
            name='course_field',
            field=models.CharField(blank=True, default='no_field', max_length=20),
        ),
    ]