from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


def get_all_notes(request) -> Response:
    notes = Note.objects.all().order_by('update')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


def get_one_note(request, note_id: int) -> Response:
    note = Note.objects.get(id=note_id)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def create_note(request) -> Response:
    create_data = request.data
    note = Note.objects.create(body=create_data['body'])
    serializer = NoteSerializer(instance=note, many=False)
    return Response(serializer.data)


def update_note(request, note_id: int) -> Response:
    update_data = request.data
    note = Note.objects.get(id=note_id)
    serializer = NoteSerializer(instance=note, data=update_data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


def delete_note(request, note_id: int) -> Response:
    note = Note.objects.get(id=note_id)
    note.delete()
    return Response('Note has been deleted')
