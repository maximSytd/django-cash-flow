from django import forms
import django_filters
import django_filters.widgets
from django.utils.translation import gettext_lazy as _

from ..models import MoneyFlow, MoneyFlowStatus, Category, CategoryType


class MoneyFlowFilter(django_filters.FilterSet):
    """Represent MoneyFlow list filterset."""

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        if user:
            self.filters["status"].queryset = user.money_flow_statuses.all()
            self.filters["category"].queryset = user.categories.all()
            self.filters["category_type"].queryset = user.category_types.all()

    total_sum = django_filters.RangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={
                "class": "form-control",
                "placeholder": _("Min / Max"),
                "step": 10,
                "type": "float",
                "min": MoneyFlow.TOTAL_SUM_MIN_VALUE,
                "max": MoneyFlow.TOTAL_SUM_MAX_VALUE,
            }
        ),
        label=_("Amount (range)"),
    )
    status = django_filters.ModelChoiceFilter(
        queryset=MoneyFlowStatus.objects.none(),
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
        ),
        label=_("Status"),
    )
    def filter_category_tree(queryset, name, value):
        """
        Return query set of tree search of descendant categories,
        self included.
        """
        if not value:
            return queryset
        return queryset.filter(
            category__in=value.get_descendants(
                include_self=True,
            ),
        )
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.none(),
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "id": "id_category_select",
            },
        ),
        label=_("Category"),
        empty_label=_("Choose category"),
        method=filter_category_tree,
    )
    category_type = django_filters.ModelChoiceFilter(
        queryset=CategoryType.objects.none(),
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "id_category_type_select",
                "placeholder": _("Search by category type"),
            },
        ),
        label=_("Category type"),
        field_name="category__type",
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
            "category_type",
            "category",
            "created",
        )