from django.db import models
from django.conf import settings
from django_extensions.db.fields import AutoSlugField

User = settings.AUTH_USER_MODEL


class Project(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150, null=True)
    handle = AutoSlugField(populate_from="title", null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
