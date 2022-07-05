from django.urls import path
from api import views

# Define urls and connect it with views
urlpatterns = [
    path('', views.get_routes, name="routes"),
    path('notes/', views.get_notes, name="notes"),
]