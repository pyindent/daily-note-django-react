# Generated by Django 4.2.1 on 2024-11-20 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_audio_files_delete_audio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='audio_files',
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(upload_to='audio/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audio_files', to='notes.note')),
            ],
        ),
    ]
