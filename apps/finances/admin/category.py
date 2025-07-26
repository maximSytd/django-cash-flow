from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from ..models import Category
from apps.core.admin import BaseAdmin


@admin.register(Category)
class CategoryAdmin(BaseAdmin, DraggableMPTTAdmin):
    """Admin ui model for Category."""

    list_display = (
        "tree_actions",
        "indented_title",
        "type",
        "user"
    )
    list_display_links = (
        "indented_title",
    )
    search_fields = (
        "title",
    )

    fields = (
        "title",
        "parent",
        "type",
        "user"
    )
    mptt_level_indent = 10
