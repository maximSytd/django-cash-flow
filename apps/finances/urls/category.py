from django.urls import path

from ..views import (
    CategoryCreateView,
    CategoryListView,
    CategoryUpdateView,
    CategoryDeleteView,
)

urlpatterns = [
    path(
        "create/",
        CategoryCreateView.as_view(),
        name="create",
    ),
    path(
        "list/",
        CategoryListView.as_view(),
        name="list",
    ),
    path(
        "<int:pk>/update/",
        CategoryUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="delete",
    ),
]
