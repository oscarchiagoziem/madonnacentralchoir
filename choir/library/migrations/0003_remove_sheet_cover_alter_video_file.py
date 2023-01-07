# Generated by Django 4.0.4 on 2023-01-06 21:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_audio_composer_alter_audio_part_of_calender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sheet',
            name='cover',
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='Videos/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mp4', 'mov', 'flv', 'avi'])]),
        ),
    ]
