from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.core.models import BaseModel

class MoneyFlow(BaseModel):
    """Represent Money flow in db."""

    total_sum = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Total sum"),
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100_000_000),
        ]
    )
    status = models.ForeignKey(
        to="finances.MoneyFlowStatus",
        related_name="money_flows",
        on_delete=models.RESTRICT,
        verbose_name=_("Status"),
    )
    category = models.ForeignKey(
        to="finances.Category",
        related_name="money_flows",
        on_delete=models.RESTRICT,
        verbose_name=_("Category"),
    )
    comment = models.TextField(
        null=True,
        blank=True,
        max_length=500,
        verbose_name=_("Comment"),
    )
    user = models.ForeignKey(
        to="users.User",
        related_name="money_flows",
        on_delete=models.RESTRICT,
        verbose_name=_("User"),
    )

    # objects = ...

    class Meta:
        verbose_name = _("Money flow")
        verbose_name_plural = _("Money flows")

    def __str__(self) -> str:
        return f"{self.flow_type} ({self.status.title})"
