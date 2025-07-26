from django import forms
import django_filters
import django_filters.widgets
from django.utils.translation import gettext_lazy as _

from ..models import MoneyFlow, MoneyFlowStatus, Category, CategoryType


class MoneyFlowFilter(django_filters.FilterSet):
    """Represent MoneyFlow list filterset."""

    total_sum = django_filters.RangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={
                "class": "form-control",
                "placeholder": _("Min / Max"),
                "step": "10",
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
        queryset=Category.objects.none(),
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
        ),
        label=_("Category"),
    )

    category_type = django_filters.ModelChoiceFilter(
        queryset=CategoryType.objects.all(),
        lookup_expr="icontains",
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "placeholder": _("Search by category type"),
            },
        ),
        label=_("Category type"),
        method=...,
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
            "created",
        )