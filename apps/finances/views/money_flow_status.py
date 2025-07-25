from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from ..models import MoneyFlowStatus
from ..forms import MoneyFlowStatusForm


class MoneyFlowStatusListView(LoginRequiredMixin, ListView):
    model = MoneyFlowStatus
    context_object_name = "money_flow_statuses"
    queryset = MoneyFlowStatus.objects.order_by("created")


class MoneyFlowStatusCreateView(LoginRequiredMixin, CreateView):
    model = MoneyFlowStatus
    form_class = MoneyFlowStatusForm
    success_url = reverse_lazy("finances:money_flow_statuses_list")


class MoneyFlowStatusUpdateView(LoginRequiredMixin, UpdateView):
    model = MoneyFlowStatus
    form_class = MoneyFlowStatusForm
    success_url = reverse_lazy("finances:money_flow_statuses_list")


class MoneyFlowStatusDeleteView(LoginRequiredMixin, DeleteView):
    model = MoneyFlowStatus
    success_url = reverse_lazy("finances:money_flow_statuses_list")


class RemoveUserMoneyFlowStatusView(LoginRequiredMixin, View):
    """
    Remove a money flow status from the user's selected statuses
    without deleting it from the database.
    """

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        status_id = kwargs.get("pk")
        status = get_object_or_404(MoneyFlowStatus, pk=status_id)

        request.user.money_flow_statuses.remove(status)
        return HttpResponseRedirect(
            reverse_lazy("finances:money_flow_statuses_list")
        )