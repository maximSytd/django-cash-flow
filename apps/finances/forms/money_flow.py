from django import forms
from django.utils.translation import gettext_lazy as _

from mptt.forms import TreeNodeChoiceField

from ..models import MoneyFlow, MoneyFlowStatus, Category


class MoneyFlowForm(forms.ModelForm):
    """Form for creating/updating MoneyFlow."""

    total_sum = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control w-25",
                "placeholder": _("Enter amount"),
                "step": "0.01",
                "min": "1",
                "max": "100000000",
            }
        ),
        label=_("Amount"),
        max_digits=12,
        decimal_places=2,
    )

    status = forms.ModelChoiceField(
        queryset=MoneyFlowStatus.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "select2 form-select w-50",
                "data-placeholder": _("Select status"),
            }
        ),
        label=_("Status"),
    )

    category = TreeNodeChoiceField(
        queryset=Category.objects.order_by("tree_id", "lft"),
        level_indicator = "-",
        widget=forms.Select(
            attrs={
                "class": "select2 form-select w-50",
                "data-placeholder": _("Select category"),
            }
        ),
        label=_("Category"),
    )

    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control w-50",
                "placeholder": _("Optional comment"),
                "rows": 3,
            }
        ),
        label=_("Comment"),
        required=False,
    )

    class Meta:
        model = MoneyFlow
        fields = (
            "total_sum",
            "status",
            "category",
            "comment",
        )
