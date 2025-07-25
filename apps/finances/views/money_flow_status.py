from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.core.views import OwnerAccessMixin
from ..models import MoneyFlowStatus
from ..forms import MoneyFlowStatusForm


class MoneyFlowStatusListView(LoginRequiredMixin, ListView):
    model = MoneyFlowStatus
    context_object_name = "money_flow_statuses"
    template_name = "finances/money_flow_status/list.html"

    def get_queryset(self):
        """Return view queryset."""
        return self.request.user.money_flow_statuses.order_by("created")


class MoneyFlowStatusCreateView(LoginRequiredMixin, CreateView):
    model = MoneyFlowStatus
    form_class = MoneyFlowStatusForm
    success_url = reverse_lazy("finances:money_flow_status:list")
    template_name = "finances/money_flow_status/create.html"

    def get_form_kwargs(self):
        """Return form kwargs expended with user."""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class MoneyFlowStatusUpdateView(
    LoginRequiredMixin,
    OwnerAccessMixin,
    UpdateView,
):
    model = MoneyFlowStatus
    form_class = MoneyFlowStatusForm
    success_url = reverse_lazy("finances:money_flow_status:list")
    template_name = "finances/money_flow_status/update.html"

    def get_form_kwargs(self):
        """Return form kwargs expended with user."""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class RemoveUserMoneyFlowStatusView(
    LoginRequiredMixin,
    OwnerAccessMixin,
    DeleteView,
):
    model = MoneyFlowStatus
    success_url = reverse_lazy("finances:money_flow_status:list")
