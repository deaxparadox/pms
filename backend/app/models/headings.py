import datetime
from datetime import (
    datetime, time, date
)
from django.db import models
from django.urls import reverse

class Heading(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    heading = models.CharField(max_length=255)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.heading
    
    def get_absolute_url(self):
        return reverse("app:edit_heading_view", kwargs={"id": self.id})
    