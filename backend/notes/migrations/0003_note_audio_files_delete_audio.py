# Generated by Django 4.2.1 on 2024-11-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='audio_files',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
    ]
