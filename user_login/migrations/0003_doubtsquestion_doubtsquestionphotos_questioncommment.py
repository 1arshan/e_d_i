# Generated by Django 3.0.8 on 2020-07-09 15:23

from django.db import migrations, models
import django.db.models.deletion
import user_login.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject_material', '0004_remove_notesmaterial_testing'),
        ('user_login', '0002_auto_20200709_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoubtsQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doubts_question', models.TextField()),
                ('material_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_material.VideoMaterial')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionCommment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=256)),
                ('question_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_login.DoubtsQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='DoubtsQuestionPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=user_login.models.renaming_uploaded_file1)),
                ('doubts_question_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_login.DoubtsQuestion')),
            ],
        ),
    ]
