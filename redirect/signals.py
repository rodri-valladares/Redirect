from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core import cache

from .models import Redirect


@receiver(post_save, sender=Redirect)
def save_cache(sender, instance, **kwargs):
    cache.set(instance.key, instance)