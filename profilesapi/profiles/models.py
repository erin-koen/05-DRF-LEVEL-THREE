from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# profile and profile status models. up till this point we've used the user
# model for authentication and to connect to other models. We'll create
# profile model here and extend the user model, using it only to authenticate
# users within the system. 


# we want to use signals to create a new instance of profile when a new 
# instance of user is created. 


class Profile(models.Model):
    # connect to the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username  # this references the username property
        # on the user entry from the OneToOne


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "statuses"

    def __str__(self):
        return str(self.user_profile)