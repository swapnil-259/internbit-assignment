import uuid6
from django.db import models

from apps.core.choices import StatusChoices
from apps.core.managers import BaseManager


class BaseModel(models.Model):
    uuid = models.UUIDField(
        unique=True, default=uuid6.uuid6, editable=False, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(
        choices=StatusChoices, default=StatusChoices.CREATE
    )

    objects = BaseManager()

    class Meta:
        abstract = True
