from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import StaffProfile

# Signal to create StaffProfile when a new User is created
@receiver(post_save, sender=User)
def create_staff_profile(sender, instance, created, **kwargs):
    if created:
        StaffProfile.objects.create(user=instance, role="receptionist")
