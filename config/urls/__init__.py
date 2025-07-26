from django.contrib import admin
from django.urls import path, include

from debug_toolbar.toolbar import debug_toolbar_urls

from apps.core.views import IndexView
from .api_versions import urlpatterns as api_urlpatterns
from .debug import urlpatterns as debug_urlpatterns


urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index",
    ),
    path(
        "users/",
        include("apps.users.urls"),
    ),
    path(
        "finances/",
        include("apps.finances.urls"),
    ),
]

urlpatterns += debug_toolbar_urls()

urlpatterns += (
        path(
            "admin/",
            admin.site.urls,
        ),
    )


urlpatterns += api_urlpatterns
urlpatterns += debug_urlpatterns
