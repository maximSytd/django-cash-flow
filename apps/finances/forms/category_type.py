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
    def clean(self):
        """Custom clean to ensure title unique."""
        cleaned_data = super().clean()
        title = cleaned_data.get("title")

        if title and CategoryType.objects.filter(
            user=self.user,
            title=title,
        ).exclude(
            pk=self.instance.pk,
        ).exists():
            self.add_error(
                "title",
                _(
                    "A category type with this title already exists.",
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
        model = CategoryType
        fields = (
            "title",
        )