from django.db import models


class StatusChoices(models.IntegerChoices):
    DELETE = 0
    CREATE = 1
    UPDATE = 2
