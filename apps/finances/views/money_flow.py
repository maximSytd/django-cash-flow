from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_filters.views import FilterView

from ..models import MoneyFlow
from ..filters import MoneyFlowFilter
from ..forms import MoneyFlowForm


class MoneyFlowFilterView(LoginRequiredMixin, FilterView):
    model = MoneyFlow
    template_name = "finances/money_flow/list.html"
    filterset_class = MoneyFlowFilter
    context_object_name = "money_flows"
    queryset = MoneyFlow.objects.all()
    paginate_by = 10


class MoneyFlowCreateView(LoginRequiredMixin, CreateView):
    model = MoneyFlow
    template_name = "finances/money_flow/create.html"
    form_class = MoneyFlowForm
    success_url = reverse_lazy("finances:money_flow:list")

    def form_valid(self, form):
        """Return validated form."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class MoneyFlowDetailView(LoginRequiredMixin, DetailView):
    model = MoneyFlow
    template_name = "finances/money_flow/detail.html"
    context_object_name = "money_flow"
    queryset = MoneyFlow.objects.all()


class MoneyFlowDeleteView(LoginRequiredMixin, DeleteView):
    model = MoneyFlow
    success_url = reverse_lazy("finances:money_flow:list")


class MoneyFlowUpdateView(LoginRequiredMixin, UpdateView):
    model = MoneyFlow
    template_name = "finances/money_flow/update.html"
    form_class = MoneyFlowForm
    context_object_name = "money_flow"

    def get_success_url(self):
        return reverse_lazy(
            "finances:detail_money_flow",
            kwargs={
                "pk": self.object.pk,
            },
        )

