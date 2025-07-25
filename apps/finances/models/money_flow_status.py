from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel

class MoneyFlowStatus(BaseModel):
    """Represent Money flow status in db."""

    title = models.CharField(
        unique=True,
        max_length=120,
        verbose_name=_("Title"),
    )

    class Meta:
        verbose_name = _("Money flow status")
        verbose_name_plural = _("Money flow statuses")

    def __str__(self) -> str:
        return f"{self.title}"
