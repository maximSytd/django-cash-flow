from django import forms
import django_filters
import django_filters.widgets
from django.utils.translation import gettext_lazy as _

from ..models import MoneyFlow, MoneyFlowStatus, Category


class MoneyFlowFilter(django_filters.FilterSet):
    """Represent MoneyFlow list filterset."""

    total_sum = django_filters.RangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={
                "class": "form-control",
                "placeholder": _("Min / Max"),
                "step": "0.01",
                "type": "number",
            },
        ),
        label=_("Amount (range)"),
    )

    status = django_filters.ModelChoiceFilter(
        queryset=MoneyFlowStatus.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
        ),
        label=_("Status"),
    )

    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
        ),
        label=_("Category"),
    )

    comment = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": _("Search by comment"),
            },
        ),
        label=_("Comment"),
    )

    created = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={
                "type": "date",
                "class": "form-control",
            },
        ),
        label=_("Created date (range)"),
    )

    class Meta:
        model = MoneyFlow
        fields = (
            "total_sum",
            "status",
            "category",
            "comment",
            "created",
        )