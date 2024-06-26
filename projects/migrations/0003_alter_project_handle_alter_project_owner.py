# Generated by Django 5.0.2 on 2024-03-29 20:07

import django.db.models.deletion
import django_extensions.db.fields
import projects.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_project_added_by_project_added_by_username_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="handle",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                editable=False,
                null=True,
                populate_from="title",
                unique=True,
                validators=[projects.validators.validate_project_handle],
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="owned_projects",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
