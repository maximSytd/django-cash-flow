from django.urls import include, path

app_name = "finances"

urlpatterns = [
    path(
        "categories/",
        include(
            "finances.urls.category",
            namespace="category",
        ),
    ),
    path(
        "categories-types/",
        include(
            "finances.urls.category_type",
            namespace="category_type",
        ),
    ),
    path(
        "statuses/",
        include(
            "finances.urls.money_flow_status",
            namespace="money_flow_status",
        ),
    ),
    path(
        "money-flow/",
        include(
            "finances.urls.money_flow",
            namespace="money_flow",
        ),
    ),
]
