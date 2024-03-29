from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from projects import views
from django.conf.urls.static import static

urlpatterns = [
    path(
        "activate/project/<slug:handle>",
        views.activate_project_view,
    ),
    path(
        "deactivate/project/<slug:handle>",
        views.deactivate_project_view,
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
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
