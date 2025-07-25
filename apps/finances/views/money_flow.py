from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_filters.views import FilterView

from apps.core.views import OwnerAccessMixin
from ..models import MoneyFlow
from ..filters import MoneyFlowFilter
from ..forms import MoneyFlowForm


class MoneyFlowFilterView(LoginRequiredMixin, FilterView):
    model = MoneyFlow
    template_name = "finances/money_flow/list.html"
    filterset_class = MoneyFlowFilter
    context_object_name = "money_flows"
    paginate_by = 10

    def get_queryset(self):
        """Return view queryset."""
        return self.request.user.money_flows.order_by("created")


class MoneyFlowCreateView(LoginRequiredMixin, CreateView):
    model = MoneyFlow
    template_name = "finances/money_flow/create.html"
    form_class = MoneyFlowForm
    success_url = reverse_lazy("finances:money_flow:list")

    def form_valid(self, form):
        """Return validated form."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class MoneyFlowDeleteView(LoginRequiredMixin, DeleteView):
    model = MoneyFlow
    success_url = reverse_lazy("finances:money_flow:list")


class MoneyFlowUpdateView(LoginRequiredMixin, OwnerAccessMixin, UpdateView):
    model = MoneyFlow
    template_name = "finances/money_flow/update.html"
    form_class = MoneyFlowForm
    context_object_name = "money_flow"

    def get_success_url(self):
        return reverse_lazy("finances:money_flow:list")
