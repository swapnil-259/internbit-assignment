from django.db import models

from apps.core.choices import StatusChoices


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(status=StatusChoices.DELETE)
