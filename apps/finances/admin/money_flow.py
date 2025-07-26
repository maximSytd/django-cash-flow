from django.contrib import admin

from ..models import MoneyFlow
from apps.core.admin import BaseAdmin


@admin.register(MoneyFlow)
class MoneyFlowAdmin(BaseAdmin):
    """Admin UI model for MoneyFlow."""

    list_display = (
        "user",
        "total_sum",
        "status",
        "category",
        "created",
    )
    list_filter = (
        "status",
        "category__type",
        "created",
    )
    search_fields = (
        "comment",
        "user__username",
    )
    autocomplete_fields = (
        "user",
        "category",
        "status",
    )
    date_hierarchy = "created"
    ordering = ("-created",)