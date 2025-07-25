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
    def save(self, commit=True) -> CategoryType:
        """
        Creates or gets a Category type with the title and associate it
        with the user.
        """
        title = self.cleaned_data["title"]
        instance, created = CategoryType.objects.get_or_create(title=title)
        self.user.category_types.add(instance)
        if commit:
            instance.save()
        return instance

    def validate_unique(self):
        """Removed for custom logic."""

    class Meta:
        model = CategoryType
        fields = ("title", )