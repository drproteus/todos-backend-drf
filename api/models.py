import uuid
from django.db import models

def _dashless_uuid():
    return uuid.uuid4().hex

class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=_dashless_uuid, editable=False)
    title = models.CharField(max_length=256)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
