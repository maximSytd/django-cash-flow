from apps.core.api.serializers import ModelBaseSerializer
from ...models import Category

class CategoryModelSerializer(ModelBaseSerializer):
    """Model serializer for Category model."""

    class Meta:
        model = Category
        field = (
            "id",
            "title",
        )
