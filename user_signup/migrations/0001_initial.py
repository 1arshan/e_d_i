# Generated by Django 3.0.8 on 2020-07-10 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('standard_or_class', models.CharField(max_length=10)),
                ('email_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('pincode', models.CharField(max_length=12)),
                ('date', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(blank=True, max_length=8)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TempStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('pincode', models.CharField(max_length=10)),
                ('standard_or_class', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(blank=True, max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='TempTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('description', models.TextField(blank=True)),
                ('password', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(blank=True, max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('teacher_description', models.TextField(blank=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(blank=True, max_length=8)),
                ('is_verified', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=13, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
