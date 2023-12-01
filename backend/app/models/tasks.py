from collections.abc import Iterable
from django.db import models
from django.dispatch import receiver, Signal
from django.db.models.signals import pre_save


from . headings import Heading

# task_date_exceed_heading = Signal()

class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    task = models.CharField(max_length=255)
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE, related_name="tasks")
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.task
    
    def end_bound(self):
        """
        This function checks, 
        whether task task end start exceeding headings end date.

        If task date exceeds headings end date, if return True, 
        else return False.
        """
        return self.end > self.heading.end

    def save(self, *args, **kwargs) -> None:
        return super().save(*args, **kwargs)
    
