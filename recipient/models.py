from django.db import models


# Create your models here.
class Recipient(models.Model):
    email = models.EmailField(null=False, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.email}"
