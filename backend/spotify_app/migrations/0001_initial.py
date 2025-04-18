# Generated by Django 3.2 on 2025-04-03 01:43

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('album', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('spotify_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('songs', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to='spotify_app.song')),
            ],
        ),
    ]
