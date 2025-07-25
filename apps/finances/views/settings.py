from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class TransactionSettingsView(LoginRequiredMixin, TemplateView):
    """Class-based view for transaction settings page."""

    template_name = "finances/settings.html"
