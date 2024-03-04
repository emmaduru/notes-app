from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from .models import Note

# Create your tests here.
class NoteTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret"
        )
        self.note = Note.objects.create(
            text="My first note",
            author=self.user
        )
        self.client = Client()

    def test_string_representation(self):
        note = Note(text="A note")
        self.assertEqual(str(note), note.text)

    def test_note_content(self):
        self.assertEqual(f"{self.note.text}", "My first note")
        self.assertEqual(f"{self.note.author}", "testuser")

    def test_note_list_view_logged_out(self):
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/users/login/?next=/notes/")

    def test_note_list_view_logged_in(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My first note")
        self.assertTemplateUsed(response, "note_list.html")

    def test_note_create_view_logged_out(self):
        response = self.client.post(reverse("note_create"), {
            "text": "New note",
            "author": self.user,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/users/login/?next=/notes/create/")

    def test_note_create_view_logged_in(self):
        self.client.force_login(user=self.user)
        response = self.client.post(reverse("note_create"), {
            "text": "New note",
            "author": self.user,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("note_list"))

    def test_note_update_view_logged_out(self):
        response = self.client.post(reverse("note_edit", args="1"), {
            "text": "New note updated",
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/users/login/?next=/notes/1/edit/")

    def test_note_update_view_logged_in(self):
        self.client.force_login(user=self.user)
        response = self.client.post(reverse("note_edit", args="1"), {
            "text": "New note updated",
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("note_list"))


    def test_note_delete_view_logged_out(self):
        response = self.client.post(reverse("note_delete", args="1"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/users/login/?next=/notes/1/delete/")

    def test_note_delete_view_logged_in(self):
        self.client.force_login(user=self.user)
        response = self.client.post(reverse("note_delete", args="1"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("note_list"))