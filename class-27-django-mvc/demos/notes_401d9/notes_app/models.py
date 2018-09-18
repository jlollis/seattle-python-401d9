from django.db import models


class Note(models.Model):
    STATES = [
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
    ]

    title = models.CharField(max_length=48)
    description = models.CharField(max_length=4096)
    status = models.CharField(choices=STATES, default='incomplete', max_length=48)

    def __str__(self):
        return f'Note: {self.title} ({self.status})'

    def __repr__(self):
        return f'Note: {self.title} ({self.status})'
