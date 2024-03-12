from django.db import models
from django.conf import settings
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class AnonymousProject:
    value = None
    is_activated = False


class Project(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    # description
    handle = AutoSlugField(populate_from="title", null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"handle": self.handle})

    @property
    def is_activated(self):
        return True
