import uuid
from django.db import models
from django.conf import settings


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    order = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def url(self):
        return "{}/todos/{}/".format(settings.BASE_URL, self.id)
