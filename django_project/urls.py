from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from projects import views

urlpatterns = [
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
    path("admin/", admin.site.urls),
    # Packages
    path("accounts/", include("allauth.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    # apps
    path("", include("pages.urls")),
    path("projects/", include("projects.urls")),
    path("items/", include("items.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
