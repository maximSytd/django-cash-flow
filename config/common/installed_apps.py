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

THIRD_PARTY = (
    "imagekit",
    "django_filters",
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

INSTALLED_APPS += THIRD_PARTY + LOCAL_APPS