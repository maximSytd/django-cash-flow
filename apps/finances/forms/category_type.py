from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import CategoryType


class CategoryTypeForm(forms.ModelForm):
    """Form for creating/updating CategoryType."""

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
    def save(self) -> CategoryType:
        """
        Creates or gets a Category type with the title and associate it
        with the user.
        """
        title = self.cleaned_data["title"]
        instance, _ = CategoryType.objects.get_or_create(title=title)
        self.user.categories.add(instance)
        return instance

    class Meta:
        model = CategoryType
        fields = ("title", )