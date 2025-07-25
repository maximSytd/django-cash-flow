from django import forms
from django.utils.translation import gettext_lazy as _

from mptt.forms import TreeNodeChoiceField

from ..models import Category, CategoryType


class CategoryForm(forms.ModelForm):
    """Form for creating/updating Category."""

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

    slug = forms.SlugField(
        widget=forms.TextInput(attrs={
            "class": "form-control w-50",
            "placeholder": _("Enter URL-friendly slug")
        }),
        label=_("Slug"),
        max_length=100
    )

    type = forms.ModelChoiceField(
        queryset=CategoryType.objects.all(),
        widget=forms.Select(attrs={
            "class": "form-select w-50",
            "data-placeholder": _("Select category type")
        }),
        label=_("Type"),
    )

    def save(self) -> Category:
        """
        Creates or gets a Category with the title and associate it
        with the user.
        """
        title = self.cleaned_data["title"]
        instance, _ = Category.objects.get_or_create(title=title)
        self.user.categories.add(instance)
        return instance

    class Meta:
        model = Category
        fields = (
            "title",
            "parent",
            "slug",
            "type",
        )
