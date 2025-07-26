from django.urls import path

from .views import CategoryByTypeAPIView

urlpatterns = [
    path(
        "categories/by-type/",
        CategoryByTypeAPIView.as_view(),
        name="categories_by_type",
    ),
]