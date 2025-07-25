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

    def save(self, commit=True) -> MoneyFlowStatus:
        """
        Creates or gets a Money flow status with the title and associate it
        with the user.
        """
        title = self.cleaned_data["title"]
        instance, _ = MoneyFlowStatus.objects.get_or_create(title=title)
        self.user.money_flow_statuses.add(instance)
        if commit:
            instance.save()
        return instance

    def validate_unique(self):
        """Removed for custom logic."""

    class Meta:
        model = MoneyFlowStatus
        fields = ("title", )