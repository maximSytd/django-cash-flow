from django.urls import path

from ..views import (
    CategoryTypeCreateView,
    CategoryTypeListView,
    CategoryTypeUpdateView,
    RemoveUserCategoryTypeView,
)

urlpatterns = [
    path(
        "create/",
        CategoryTypeCreateView.as_view(),
        name="create",
    ),
    path(
        "list/",
        CategoryTypeListView.as_view(),
        name="list",
    ),
    path(
        "<int:pk>/update/",
        CategoryTypeUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/remove/",
        RemoveUserCategoryTypeView.as_view(),
        name="remove",
    ),
]