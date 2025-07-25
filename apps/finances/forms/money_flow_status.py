from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import MoneyFlowStatus


class MoneyFlowStatusForm(forms.ModelForm):
    """Form for creating/updating MoneyFlowStatus."""

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-50",
                "placeholder": _("Enter status name"),
            },
        ),
        label=_("Title"),
        max_length=120,
    )
    user = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False,
    )

    class Meta:
        model = MoneyFlowStatus
        fields = (
            "title",
            "user",
        )