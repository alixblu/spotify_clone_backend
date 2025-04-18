# Generated by Django 3.2 on 2025-04-09 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('album_name', models.CharField(max_length=255)),
                ('file_path', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.user')),
                ('songs', models.ManyToManyField(to='music_library.Song')),
            ],
        ),
    ]
