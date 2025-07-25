from django.urls import include, path

app_name = "finances"

urlpatterns = [
    path(
        "categories/",
        include(
            (
                "apps.finances.urls.category",
                "category",
            ),
        ),
    ),
    path(
        "categories-types/",
        include(
            (
                "apps.finances.urls.category_type",
                "category_type",
            ),
        ),
    ),
    path(
        "statuses/",
        include(
            (
                "apps.finances.urls.money_flow_status",
                "money_flow_status",
            ),
        ),
    ),
    path(
        "money-flow/",
        include(
            (
                "apps.finances.urls.money_flow",
                "money_flow",
            ),
        ),
    ),
]
