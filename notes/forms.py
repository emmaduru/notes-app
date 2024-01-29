from django import forms

class NoteCreateForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea(attrs={"rows":"5"}), required=True)

class NoteUpdateForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea(attrs={"rows":"5"}), required=True)