from rest_framework.serializers import ModelSerializer
from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        # fields = ['body', 'update'] - for specific fields
        fields = '__all__'

