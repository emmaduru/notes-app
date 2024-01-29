from django.urls import path
from .views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path("create/", NoteCreateView.as_view(), name="note_create"),
    path("<int:pk>/edit/", NoteUpdateView.as_view(), name="note_edit"),
    path("<int:pk>/delete", NoteDeleteView.as_view(), name="note_delete"),
    path("", NoteListView.as_view(), name="note_list")
]