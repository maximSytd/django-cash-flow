from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from apps.finances.models import CategoryType, MoneyFlowStatus

@receiver(post_save, sender=User)
def create_default_related_models(sender, instance, created, **kwargs):
    """Creates related business entities by default."""
    if not created:
        return

    if not instance.category_types.exists():
        CategoryType.objects.bulk_create(
            [
                CategoryType(title="Пополнение", user=instance),
                CategoryType(title="Списание", user=instance),
            ],
        )

    if not instance.money_flow_statuses.exists():
        MoneyFlowStatus.objects.bulk_create(
            [
                MoneyFlowStatus(title="Бизнес", user=instance),
                MoneyFlowStatus(title="Личное", user=instance),
                MoneyFlowStatus(title="Налог", user=instance),
            ],
        )