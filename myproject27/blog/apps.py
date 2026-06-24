from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'


    def ready(self):
        import blog.signals  # import signals to ensure they are regiter