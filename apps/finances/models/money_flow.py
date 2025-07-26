from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.core.models import BaseModel


class MoneyFlow(BaseModel):
    """Represent Money flow in db."""

    TOTAL_SUM_MIN_VALUE = 0
    TOTAL_SUM_MAX_VALUE = 100_000_000

    total_sum = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Total sum"),
        validators=[
            MinValueValidator(TOTAL_SUM_MIN_VALUE),
            MaxValueValidator(TOTAL_SUM_MAX_VALUE),
        ]
    )
    status = models.ForeignKey(
        to="finances.MoneyFlowStatus",
        related_name="money_flows",
        on_delete=models.CASCADE,
        verbose_name=_("Status"),
    )
    category = models.ForeignKey(
        to="finances.Category",
        related_name="money_flows",
        on_delete=models.CASCADE,
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
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )
    created = models.DateTimeField(
        verbose_name=_("Created"),
        default=timezone.now,
        blank=True,
        null=True
    )

    # objects = ...

    class Meta:
        verbose_name = _("Money flow")
        verbose_name_plural = _("Money flows")

    def __str__(self) -> str:
        return f"{self.total_sum} ({self.status.title})"
