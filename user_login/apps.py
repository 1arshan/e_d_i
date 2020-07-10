from django.apps import AppConfig


class UserLoginConfig(AppConfig):
    name = 'user_login'

    def ready(self):
        import user_login.signals