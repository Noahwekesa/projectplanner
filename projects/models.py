from django.db import models
from django.conf import settings
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
from . import validators

User = settings.AUTH_USER_MODEL


class AnonymousProject:
    value = None
    is_activated = False


class Project(models.Model):
    owner = models.ForeignKey(
        User,
        null=True,
        related_name="owned_projects",
        on_delete=models.SET_NULL,
    )
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    handle = AutoSlugField(
        populate_from="title",
        null=True,
        blank=True,
        unique=True,
        validators=[validators.validate_project_handle],
    )
    active = models.BooleanField(default=True)

    added_by = models.ForeignKey(
        User,
        related_name="projects_added",
        on_delete=models.SET_NULL,
        null=True,
    )
    added_by_username = models.CharField(max_length=120, null=True, blank=True)
    last_modified_by = models.ForeignKey(
        User,
        related_name="projects_changed",
        on_delete=models.SET_NULL,
        null=True,
    )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"handle": self.handle})

    @property
    def is_activated(self):
        return True

    def save(self, *args, **kwargs):
        if self.added_by:
            self.added_by_username = self.added_by.username
        super().save(*args, **kwargs)
