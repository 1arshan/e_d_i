from django.apps import AppConfig


class SubjectMaterialConfig(AppConfig):
    name = 'subject_material'

    def ready(self):
        import subject_material.signals