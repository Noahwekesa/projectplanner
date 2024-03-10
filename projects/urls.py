from django.urls import path

from . import views

urlpatterns = [
    path("projects/", views.projects_view, name="projects"),
    path(
        "activate/projects/<slug:handle>",
        views.activate_project_view,
        name="activate-project",
    ),
    path(
        "deactivate/projects/<slug:handle>",
        views.deactivate_project_view,
        name="activate-project",
    ),
]
