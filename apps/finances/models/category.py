from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey

from apps.core.models import BaseModel

class Category(BaseModel, MPTTModel):
    """Represent Category in db."""

    title = models.CharField(
        max_length=120,
        verbose_name=_("Title"),
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name=_("Children"),
        verbose_name=_("Parent category"),
    )
    type = models.ForeignKey(
        to="finances.CategoryType",
        related_name="categories",
        on_delete=models.CASCADE,
        verbose_name=_("Type"),
    )
    user = models.ForeignKey(
        to="users.User",
        related_name="categories",
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )

    class MPTTMeta:
        order_insertion_by = ("title",)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "user"],
                name="unique_category_per_user",
            )
        ]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self) -> str:
        if self.parent:
            return f"{self.title}-{self.parent.title}"
        return f"{self.title}"
