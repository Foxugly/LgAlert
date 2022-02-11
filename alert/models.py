from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Alert(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    created = models.DateField(default=timezone.now)

    def __str__(self):
        return f"[{self.id}] {self.title}"
