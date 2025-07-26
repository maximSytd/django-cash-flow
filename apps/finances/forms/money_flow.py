from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from mptt.forms import TreeNodeChoiceField

from ..models import MoneyFlow, MoneyFlowStatus, Category


class MoneyFlowForm(forms.ModelForm):
    """Form for creating/updating MoneyFlow."""

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields["status"].queryset = user.money_flow_statuses.all()
        self.fields["category"].queryset = user.categories.all(
        ).order_by(
            "tree_id",
            "lft",
        )

    total_sum = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control w-50",
                "placeholder": _("Enter amount in rubles"),
                "step": 10,
                "type": "float",
                "min": MoneyFlow.TOTAL_SUM_MIN_VALUE,
                "max": MoneyFlow.TOTAL_SUM_MAX_VALUE,
            }
        ),
        label=_("Amount"),
        max_digits=12,
        decimal_places=2,
    )

    status = forms.ModelChoiceField(
        queryset=MoneyFlowStatus.objects.none(),
        widget=forms.Select(
            attrs={
                "class": "select2 form-select w-50",
                "data-placeholder": _("Select status"),
            }
        ),
        label=_("Status"),
    )

    category = TreeNodeChoiceField(
        queryset=Category.objects.none(),
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
    created = forms.DateTimeField(
        initial=timezone.now,
        widget=forms.DateTimeInput(
            attrs={
                'type': "datetime-local",
                'class': "form-control",
            }
        ),
        required=True,
    )
    def save(self, commit=True):
        """Custom method to save user with form."""
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance

    class Meta:
        model = MoneyFlow
        fields = (
            "total_sum",
            "status",
            "category",
            "comment",
            "created",
        )
