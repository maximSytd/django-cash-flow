from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import CategoryType


class CategoryTypeForm(forms.ModelForm):
    """Form for creating/updating CategoryType."""

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-50",
                "placeholder": _("Enter type name"),
            },
        ),
        label=_("Title"),
        max_length=120
    )
    user = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False,
    )

    class Meta:
        model = CategoryType
        fields = (
            "title",
            "user",
        )