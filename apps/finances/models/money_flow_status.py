from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel

class MoneyFlowStatus(BaseModel):
    """Represent Money flow status in db."""

    title = models.CharField(
        max_length=120,
        verbose_name=_("Title"),
    )
    user = models.ForeignKey(
        to="users.User",
        related_name="money_flow_statuses",
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "user"],
                name="unique_money_flow_status_per_user",
            )
        ]
        verbose_name = _("Money flow status")
        verbose_name_plural = _("Money flow statuses")

    def __str__(self) -> str:
        return f"{self.title}"
