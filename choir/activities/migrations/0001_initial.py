# Generated by Django 4.0.4 on 2022-06-10 13:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=10000, verbose_name='description')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.ImageField(upload_to='gallery')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Galleries',
                'ordering': ('-uploaded_at',),
            },
        ),
        migrations.CreateModel(
            name='Act_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=10000, verbose_name='description')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='Activity_videos/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'flv'])])),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-uploaded_at',),
            },
        ),
    ]