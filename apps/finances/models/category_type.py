from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel

class CategoryType(BaseModel):
    """Represent Category type in db."""

    title = models.CharField(
        unique=True,
        max_length=120,
        verbose_name=_("Title"),
    )

    class Meta:
        verbose_name = _("Category type")
        verbose_name_plural = _("Category types")

    def __str__(self) -> str:
        return f"{self.title}"
