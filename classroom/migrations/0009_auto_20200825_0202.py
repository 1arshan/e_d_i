# Generated by Django 3.0.8 on 2020-08-24 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0008_auto_20200825_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtestquestion',
            name='class_link',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_link_test', to='classroom.ClassTest'),
        ),
    ]