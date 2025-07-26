from django.contrib import admin

from ..models import MoneyFlowStatus
from apps.core.admin import BaseAdmin


@admin.register(MoneyFlowStatus)
class MoneyFlowStatusAdmin(BaseAdmin):
    """Admin UI model for MoneyFlowStatus."""

    list_display = (
        "title",
        "user",
    )
    search_fields = (
        "title",
    )
    autocomplete_fields = (
        "user",
    )