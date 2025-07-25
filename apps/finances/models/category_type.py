from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel

class CategoryType(BaseModel):
    """Represent Category type in db."""

    title = models.CharField(
        max_length=120,
        verbose_name=_("Title"),
    )
    user = models.ForeignKey(
        to="users.User",
        related_name="category_types",
        on_delete=models.RESTRICT,
        verbose_name=_("User"),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "user"],
                name="unique_category_type_per_user",
            )
        ]
        verbose_name = _("Category type")
        verbose_name_plural = _("Category types")

    def __str__(self) -> str:
        return f"{self.title}"
