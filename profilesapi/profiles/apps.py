from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'

# this function creaded to enable signals.
    def ready(self):
        import profiles.signals
