# Generated by Django 3.0.8 on 2020-07-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0003_doubtsquestion_doubtsquestionphotos_questioncommment'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubtsquestion',
            name='is_answered',
            field=models.BooleanField(default=False),
        ),
    ]
