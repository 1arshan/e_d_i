# Generated by Django 3.0.8 on 2020-07-10 19:34

from django.db import migrations, models
import django.db.models.deletion
import user_login.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject_material', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='DoubtsAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doubts_answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DoubtsAnswerPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=user_login.models.renaming_uploaded_file2)),
            ],
        ),
        migrations.CreateModel(
            name='DoubtsQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doubts_question', models.TextField()),
                ('is_answered', models.BooleanField(default=False)),
                ('material_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_material.VideoMaterial')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=256)),
                ('question_link_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_comment_link', to='user_login.DoubtsQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='DoubtsQuestionPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=user_login.models.renaming_uploaded_file1)),
                ('question_link_photos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_photos_link', to='user_login.DoubtsQuestion')),
            ],
        ),
    ]
