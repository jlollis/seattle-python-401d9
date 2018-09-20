from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User


class Note(models.Model):
    STATES = [
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=48)
    description = models.CharField(max_length=4096)
    status = models.CharField(choices=STATES, default='incomplete', max_length=48)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_completed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Note: {self.title} ({self.status})'

    def __repr__(self):
        return f'Note: {self.title} ({self.status})'


@receiver(models.signals.post_save, sender=Note)
def set_note_complete_date(sender, instance, **kwargs):
    if instance.status == 'complete' and not instance.date_completed:
        instance.date_completed = timezone.now()
        instance.save()
