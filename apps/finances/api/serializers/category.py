from rest_framework import serializers

from apps.core.api.serializers import ModelBaseSerializer
from ...models import Category

class CategoryModelSerializer(ModelBaseSerializer):
    """Model serializer for Category model."""

    def get_indent_title(self, obj):
        return f"{"- " * obj.level}{obj.title}"
    indent_title = serializers.SerializerMethodField(
        method_name="get_indent_title",
    )

    class Meta:
        model = Category
        fields = (
            "id",
            "indent_title",
        )
