from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import UserProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Safely create UserProfile, handling existing profiles
    """
    if created:
        # Check if profile already exists (shouldn't, but just in case)
        if not UserProfile.objects.filter(user=instance).exists():
            UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Save UserProfile when CustomUser is saved
    """
    try:
        instance.userprofile.save()
    except UserProfile.DoesNotExist:
        # If profile doesn't exist, create it (shouldn't happen with create signal)
        UserProfile.objects.create(user=instance)