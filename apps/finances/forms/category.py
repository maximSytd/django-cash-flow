from django import forms
from django.utils.translation import gettext_lazy as _

from mptt.forms import TreeNodeChoiceField

from ..models import Category, CategoryType


class CategoryForm(forms.ModelForm):
    """Form for creating/updating Category."""

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields["type"].queryset = user.category_types.all()
        self.fields["parent"].queryset = user.categories.all()

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-50",
                "placeholder": _("Enter category name"),
            },
        ),
        label=_("Title"),
        max_length=120,
    )
    parent = TreeNodeChoiceField(
        queryset=Category.objects.none(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select w-50",
                "data-placeholder": _("Select parent category")
            },
        ),
        label=_("Parent category"),
        level_indicator="—",
    )
    type = forms.ModelChoiceField(
        queryset=CategoryType.objects.none(),
        widget=forms.Select(
            attrs={
                "class": "form-select w-50",
                "data-placeholder": _("Select category type")
            },
        ),
        label=_("Type"),
    )
    def clean(self):
        """Custom clean to ensure title unique."""
        cleaned_data = super().clean()
        title = cleaned_data.get("title")

        if title and Category.objects.filter(
            user=self.user,
            title=title,
        ).exclude(
            pk=self.instance.pk,
        ).exists():
            self.add_error(
                "title",
                _(
                    "A category with this title already exists.",
                ),
            )

        return cleaned_data

    def save(self, commit=True):
        """Custom method to save user with form."""
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Category
        fields = (
            "title",
            "parent",
            "type",
        )
