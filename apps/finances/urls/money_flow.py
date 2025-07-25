from django.urls import path

from ..views import (
    MoneyFlowCreateView,
    MoneyFlowFilterView,
    MoneyFlowDeleteView,
    MoneyFlowUpdateView,
)

urlpatterns = [
    path(
        "create/",
        MoneyFlowCreateView.as_view(),
        name="create",
    ),
    path(
        "list/",
        MoneyFlowFilterView.as_view(),
        name="list",
    ),
    path(
        "<int:pk>/update/",
        MoneyFlowUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete/",
        MoneyFlowDeleteView.as_view(),
        name="delete",
    ),
]