from django.urls import path

from ..views import (
    MoneyFlowStatusCreateView,
    MoneyFlowStatusListView,
    MoneyFlowStatusUpdateView,
    RemoveUserMoneyFlowStatusView,
)

urlpatterns = [
    path(
        "create/",
        MoneyFlowStatusCreateView.as_view(),
        name="create",
    ),
    path(
        "list/",
        MoneyFlowStatusListView.as_view(),
        name="list",
    ),
    path(
        "<int:pk>/update/",
        MoneyFlowStatusUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete/",
        RemoveUserMoneyFlowStatusView.as_view(),
        name="delete",
    ),
]
