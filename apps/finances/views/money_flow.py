from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_filters.views import FilterView

from apps.core.views import OwnerAccessMixin
from ..models import MoneyFlow
from ..filters import MoneyFlowFilter
from ..forms import MoneyFlowForm


class MoneyFlowFilterView(LoginRequiredMixin, FilterView):
    """View that provides feature to list MoneyFlow."""

    model = MoneyFlow
    template_name = "finances/money_flow/list.html"
    filterset_class = MoneyFlowFilter
    context_object_name = "money_flows"
    paginate_by = 10

    def get_queryset(self):
        """Return queryset for view."""
        return self.request.user.money_flows.prefetch_related(
            "status",
        ).prefetch_related(
            "category",
        ).order_by(
            "created",
        )

    def get_filterset_kwargs(self, filterset_class):
        """Return dict of kwargs for filterset."""
        kwargs = super().get_filterset_kwargs(filterset_class)
        kwargs["user"] = self.request.user
        return kwargs


class MoneyFlowCreateView(LoginRequiredMixin, CreateView):
    """View that provides feature to create MoneyFlow."""

    model = MoneyFlow
    template_name = "finances/money_flow/create.html"
    form_class = MoneyFlowForm
    success_url = reverse_lazy("finances:money_flow:list")

    def get_form_kwargs(self):
        """Return form kwargs expended with user."""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class MoneyFlowDeleteView(LoginRequiredMixin, OwnerAccessMixin, DeleteView):
    """View that provides feature to delete MoneyFlow."""

    model = MoneyFlow
    success_url = reverse_lazy("finances:money_flow:list")


class MoneyFlowUpdateView(LoginRequiredMixin, OwnerAccessMixin, UpdateView):
    """View that provides feature to update MoneyFlow."""

    model = MoneyFlow
    template_name = "finances/money_flow/update.html"
    form_class = MoneyFlowForm
    context_object_name = "money_flow"
    success_url = reverse_lazy("finances:money_flow:list")

    def get_form_kwargs(self):
        """Return form kwargs expended with user."""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
