from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FinancesAppConfig(AppConfig):
    """Default configuration for Finances app."""

    name = "apps.finances"
    verbose_name = _("Finances")