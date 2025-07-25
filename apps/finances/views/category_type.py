from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404

from ..models import CategoryType
from ..forms import CategoryTypeForm


class CategoryTypeListView(LoginRequiredMixin, ListView):
    model = CategoryType
    context_object_name = "category_types"
    template_name = "finances/category_type/list.html"

    def get_queryset(self):
        """Return model queryset."""
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

    def get_form_kwargs(self):
        """Return form kwargs expended with user."""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class RemoveUserCategoryTypeView(LoginRequiredMixin, View):
    """
    Remove a category type from the user's category types without deleting it
    from the DB.
    """

    template_name = "finances/category_type/remove.html"

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        category_type_id = kwargs.get("pk")
        category_type = get_object_or_404(CategoryType, pk=category_type_id)

        request.user.category_types.remove(category_type)
        return HttpResponseRedirect(
            reverse_lazy("finances:category_type:list"),
        )
