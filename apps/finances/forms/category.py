from django import forms
from django.utils.translation import gettext_lazy as _

from mptt.forms import TreeNodeChoiceField

from ..models import Category, CategoryType


class CategoryForm(forms.ModelForm):
    """Form for creating/updating Category."""

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

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
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select w-50",
            "data-placeholder": _("Select parent category")
        }),
        label=_("Parent category"),
        level_indicator="—"
    )
    type = forms.ModelChoiceField(
        queryset=CategoryType.objects.all(),
        widget=forms.Select(attrs={
            "class": "form-select w-50",
            "data-placeholder": _("Select category type")
        }),
        label=_("Type"),
    )

    def save(self, commit=True) -> Category:
        """
        Creates or gets a Category with the title and associate it
        with the user.
        """
        instance, created = Category.objects.get_or_create(
            title=self.cleaned_data["title"],
            type=self.cleaned_data["type"],
            parent=self.cleaned_data.get("parent"),
        )
        self.user.categories.add(instance)
        if commit:
            instance.save()
        return instance

    def validate_unique(self):
        """Removed for custom logic."""

    class Meta:
        model = Category
        fields = (
            "title",
            "parent",
            "type",
        )
