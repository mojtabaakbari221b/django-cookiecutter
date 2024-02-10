import string
from django.db import models
from shortuuid.django_fields import ShortUUIDField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    id = ShortUUIDField(
        length=6,
        max_length=40,
        prefix="nrq-",
        alphabet=string.ascii_lowercase + string.digits,
        primary_key=True,
        editable=False,
    )

    class Meta:
        abstract = True
