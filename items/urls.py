from django.urls import path

from . import views

app_name = "items"

urlpatterns = [
    path("create/", views.item_create_view, name="create-item"),
    path("", views.item_list_view, name="list"),
    path("<int:id>", views.item_detail_update_view, name="detail"),
]
