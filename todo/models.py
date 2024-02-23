from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Status(models.TextChoices):
    TODO = 'To Do', _('To Do')
    IN_PROGRESS = 'In Progress', _('In Progress')
    COMPLETED = 'Completed', _('Completed')

class TodoItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todo_items')
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
