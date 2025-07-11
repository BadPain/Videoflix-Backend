# Generated by Django 5.2.3 on 2025-07-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('genre', models.CharField(max_length=100)),
                ('video_file', models.FileField(upload_to='videos/')),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
