from django.views.generic import ListView, CreateView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Note
from .forms import NoteCreateForm, NoteUpdateForm

# Create your views here.
class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "note_list.html"
    context_object_name = "notes"
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = NoteCreateForm()
        context["edit_form"] = NoteUpdateForm()
        return context
    
    def get_queryset(self):
        return Note.objects.filter(author=self.request.user).order_by("-id")

class NoteCreateView(LoginRequiredMixin, CreateView):
    http_method_names = ["post"]
    model = Note
    fields = ("text",)
    success_url = reverse_lazy("note_list")
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    http_method_names = ["post"]
    model = Note
    fields = ("text",)
    success_url = reverse_lazy("note_list")
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    http_method_names = ["post"]
    model = Note
    success_url = reverse_lazy("note_list")
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

def csrf_failure(request, reason=""):
    return render(request, "403.html")