# Generated by Django 3.0.8 on 2020-07-05 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject_material', '0002_notesmaterial_question_ans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesmaterial',
            name='notes_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes_material_link', to='subject_material.VideoMaterial'),
        ),
    ]
