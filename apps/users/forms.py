from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserInitialsUpdateForm(forms.ModelForm):
    """User update form."""

    first_name = forms.CharField(
        label=_("Username"),
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-50",
            },
        ),
    )
    last_name = forms.CharField(
        label=_("last_name"),
        widget=forms.TextInput(
            attrs={
                "class": "form-control w-50",
            },
        ),
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
        )

class UserRegistrationForm(UserCreationForm):
    """Form for user registration."""

    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )
