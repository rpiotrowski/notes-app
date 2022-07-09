from django.urls import path
from api import views

# Define urls and connect it with views
urlpatterns = [
    path('', views.get_routes, name="routes"),
    path('notes/', views.get_notes, name="notes"),
    path('notes/<str:note_id>', views.get_note, name="note"),
    path('notes/<str:note_id>/update', views.update_note, name="update_note"),
    path('notes/<str:note_id>/delete', views.delete_note, name="delete_note"),
]
