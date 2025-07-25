from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404

from ..models import Category
from ..forms import CategoryForm


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = "categories"
    queryset = Category.objects.order_by("created")
    template_name = "finances/category/list.html"


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


class RemoveUserCategoryView(LoginRequiredMixin, View):
    """
    Remove a category from the user's categories without deleting it
    from the DB.
    """

    template_name = "finances/category/remove.html"

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        category_id = kwargs.get("pk")
        category = get_object_or_404(Category, pk=category_id)

        request.user.categories.remove(category)
        return HttpResponseRedirect(
            reverse_lazy("finances:category:list"),
        )
