from django.urls import path

from . import views

app_name = "items"

urlpatterns = [
    path("items/create", views.item_create_view, name="create-item"),
]
