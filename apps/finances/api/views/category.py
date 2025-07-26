from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ...models import Category
from ..serializers import CategoryModelSerializer


class CategoryByTypeAPIView(APIView):
    """Api view point that returns list of user's CategoryTypes in order."""

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Return data on GET request."""
        category_type_id = request.GET.get("type")
        if not category_type_id:
            return Response([])

        categories = Category.objects.filter(
            user=request.user,
            type_id=category_type_id
        ).order_by(
            "tree_id",
            "lft",
        )
        return Response(CategoryModelSerializer(categories, many=True).data)