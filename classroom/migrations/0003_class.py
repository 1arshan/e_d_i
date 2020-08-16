# Generated by Django 3.0.8 on 2020-08-09 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_signup', '0001_initial'),
        ('classroom', '0002_instituteteacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('institute_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Institute')),
                ('teacher_link', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user_signup.TeacherProfile')),
            ],
        ),
    ]