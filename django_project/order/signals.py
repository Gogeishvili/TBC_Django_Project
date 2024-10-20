from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import User
from .models import UserCard

@receiver(post_save, sender=User)
def create_user_card(sender, instance, created, **kwargs):
    if created:
        UserCard.objects.create(user=instance)