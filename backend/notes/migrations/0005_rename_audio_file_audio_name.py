# Generated by Django 4.2.1 on 2024-11-21 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_remove_note_audio_files_audio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio',
            old_name='audio_file',
            new_name='name',
        ),
    ]