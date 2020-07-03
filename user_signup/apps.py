from django.apps import AppConfig


class UserSignupConfig(AppConfig):
    name = 'user_signup'

    def ready(self):
        import user_signup.signals