from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Note(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text