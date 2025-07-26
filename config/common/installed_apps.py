# Application definition
INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)

DRF_PACKAGES = (
    "rest_framework",
    "django_filters",
    "knox",
    "drf_spectacular",
    "drf_standardized_errors",
)

THIRD_PARTY = (
    "imagekit",
    "django_extensions",
    "crispy_forms",
    "crispy_bootstrap5",
    "debug_toolbar",
    "mptt",
)

LOCAL_APPS = (
    "apps.core",
    "apps.users",
    "apps.finances",
)

INSTALLED_APPS += THIRD_PARTY + LOCAL_APPS + DRF_PACKAGES