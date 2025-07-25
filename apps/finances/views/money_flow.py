from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_filters.views import FilterView

from ..models import MoneyFlow
from ..filters import MoneyFlowFilter
from ..forms import MoneyFlowForm


class MoneyFlowFilterView(LoginRequiredMixin, FilterView):
    model = MoneyFlow
    template_name = ...
    filterset_class = MoneyFlowFilter
    context_object_name = "money_flows"
    queryset = MoneyFlow.objects.all()
    paginate_by = 10


class MoneyFlowCreateView(LoginRequiredMixin, CreateView):
    model = MoneyFlow
    template_name = ...
    form_class = MoneyFlowForm
    success_url = reverse_lazy("finances:create_money_flow")


class MoneyFlowUpdateView(LoginRequiredMixin, UpdateView):
    model = MoneyFlow
    template_name = ...
    form_class = MoneyFlowForm
    context_object_name = "money_flow"

    def get_success_url(self):
        return reverse_lazy(
            "finances:detail_money_flow",
            kwargs={
                "pk": self.object.pk,
            },
        )


class MoneyFlowDetailView(LoginRequiredMixin, DetailView):
    model = MoneyFlow
    template_name = ...
    context_object_name = "money_flow"
    queryset = MoneyFlow.objects.all()


class MoneyFlowDeleteView(LoginRequiredMixin, DeleteView):
    model = MoneyFlow
    success_url = reverse_lazy("finances:delete_money_flow")
