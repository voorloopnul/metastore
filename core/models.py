from django.db import models
import uuid


class Entity(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    namespace = models.SlugField(max_length=50)
    label = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    json = models.JSONField(null=True, blank=True)
    message = models.TextField(blank=True)
    ttl = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.namespace}:{self.uuid}"
