from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import CategoryType
from ..forms import CategoryTypeForm


class CategoryTypeListView(LoginRequiredMixin, ListView):
    model = CategoryType
    context_object_name = "category_types"
    template_name = "finances/category_type/list.html"

    def get_queryset(self):
        """Return view queryset."""
        return self.request.user.category_types.order_by("created")


class CategoryTypeCreateView(LoginRequiredMixin, CreateView):
    model = CategoryType
    form_class = CategoryTypeForm
    success_url = reverse_lazy("finances:category_type:list")
    template_name = "finances/category_type/create.html"

    def get_form_kwargs(self):
        """Return form kwargs expended with user."""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class CategoryTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = CategoryType
    form_class = CategoryTypeForm
    success_url = reverse_lazy("finances:category_type:list")
    template_name = "finances/category_type/update.html"

    def get_queryset(self):
        """Return view queryset."""
        return self.request.user.category_types.order_by("created")

    def get_form_kwargs(self):
        """Return form kwargs expended with user."""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class CategoryTypeDeleteView(LoginRequiredMixin, DeleteView):

    model = CategoryType
    success_url = reverse_lazy("finances:category_type:list")

    def get_queryset(self):
        """Return view queryset."""
        return self.request.user.category_types.order_by("created")
