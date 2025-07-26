from django.contrib import admin

from ..models import CategoryType
from apps.core.admin import BaseAdmin


@admin.register(CategoryType)
class CategoryTypeAdmin(BaseAdmin):
    """Admin UI model for CategoryType."""

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
