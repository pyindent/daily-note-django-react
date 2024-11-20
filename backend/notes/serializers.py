from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Note  
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'audio_files']
    