from django.conf import settings
from django.db import models
from projects.models import Project


User = settings.AUTH_USER_MODEL


class Item(models.Model):
    class ItemStatus(models.TextChoices):
        TODOS = "To Dos", "To Dos"
        INPROGRESS = "In Progress", "In Progress"
        DONE = "done", "done"

    class ItemType(models.TextChoices):
        BUG = "Bug", "Bug"
        FEATURE = "Feature", "Feature"
        TASK = "Task", "Task"

    class ItemPriority(models.TextChoices):
        LOW = "Low", "Low"
        MEDIUM = "Medium", "Medium"
        HIGH = "High", "High"

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=ItemStatus.choices,
        default=ItemStatus.TODOS,
    )
    itemtype = models.CharField(
        max_length=20,
        choices=ItemType.choices,
        default=ItemType.FEATURE,
    )
    priority = models.CharField(
        max_length=20,
        choices=ItemPriority.choices,
        default=ItemPriority.HIGH,
    )
    _status = models.CharField(
        max_length=20,
        choices=ItemStatus.choices,
        null=True,
        blank=True,
    )

    status_changed_at = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    added_by = models.ForeignKey(
        User, related_name="items_added", on_delete=models.SET_NULL, null=True
    )
    added_by_username = models.CharField(max_length=120, null=True, blank=True)
    last_modified_by = models.ForeignKey(
        User,
        related_name="items_changed",
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        if self.added_by:
            self.added_by_username = self.added_by.username
        super().save(*args, **kwargs)
