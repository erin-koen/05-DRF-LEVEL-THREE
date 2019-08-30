from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile

# post_save signal taking the user model as a sender to send a signal
# every time a user instance is saved. It's received with a function
# decorated with the receiver decorator. We'll also know if the user instance
# that sends the signal is newly created or just modified


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("Created: ", created)
    if created:
        Profile.objects.create(user=instance)