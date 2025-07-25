from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Category
from ..forms import CategoryForm


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = "categories"
    template_name = "finances/category/list.html"

    def get_queryset(self):
        """Return view queryset."""
        return self.request.user.categories.order_by("created")


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("finances:category:list")
    template_name = "finances/category/create.html"

    def get_form_kwargs(self):
        """Return form kwargs expended with user."""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("finances:category:list")
    template_name = "finances/category/update.html"

    def get_form_kwargs(self):
        """Return form kwargs expended with user."""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("finances:category:list")

    def get_queryset(self):
        """Return view queryset."""
        return self.request.user.categories.order_by("created")
