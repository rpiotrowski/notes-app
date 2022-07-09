from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)


@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all().order_by('update')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_note(request, note_id: str):
    note = Note.objects.get(id=note_id)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update_note(request, note_id: str):
    update_data = request.data
    note = Note.objects.get(id=note_id)
    serializer = NoteSerializer(instance=note, data=update_data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_note(request, note_id: str):
    note = Note.objects.get(id=note_id)
    note.delete()
    return Response('Note has been deleted')
