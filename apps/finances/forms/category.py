from django import forms
from django.utils.translation import gettext_lazy as _

from mptt.forms import TreeNodeChoiceField

from ..models import Category, CategoryType


class CategoryForm(forms.ModelForm):
    """Form for creating/updating Category."""

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields["type"].queryset = CategoryType.objects.filter(user=user)
        self.fields["parent"].queryset = Category.objects.filter(user=user)

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-50",
                "placeholder": _("Enter category name"),
            },
        ),
        label=_("Title"),
        max_length=120
    )
    parent = TreeNodeChoiceField(
        queryset=Category.objects.none(),
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select w-50",
            "data-placeholder": _("Select parent category")
        }),
        label=_("Parent category"),
        level_indicator="—"
    )
    type = forms.ModelChoiceField(
        queryset=CategoryType.objects.none(),
        widget=forms.Select(attrs={
            "class": "form-select w-50",
            "data-placeholder": _("Select category type")
        }),
        label=_("Type"),
    )
    user = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False,
    )

    class Meta:
        model = Category
        fields = (
            "title",
            "parent",
            "type",
            "user",
        )
