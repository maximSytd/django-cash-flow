from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404

from ..models import CategoryType
from ..forms import CategoryForm


class CategoryTypeListView(LoginRequiredMixin, ListView):
    model = CategoryType
    context_object_name = "category_types"
    queryset = CategoryType.objects.order_by("created")


class CategoryTypeCreateView(LoginRequiredMixin, CreateView):
    model = CategoryType
    form_class = CategoryForm
    success_url = reverse_lazy("finances:category_types_products")


class CategoryTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = CategoryType
    form_class = CategoryForm
    success_url = reverse_lazy("finances:category_types_products")


class RemoveUserCategoryTypeView(LoginRequiredMixin, View):
    """
    Remove a category type from the user's category types without deleting it
    from the DB.
    """

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        category_type_id = kwargs.get("pk")
        category = get_object_or_404(CategoryType, pk=category_type_id)

        request.user.categories.remove(category)
        return HttpResponseRedirect(
            reverse_lazy("finances:category_types_products"),
        )
