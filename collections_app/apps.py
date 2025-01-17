from django.apps import AppConfig

# Import the AppConfig class from Django to define
# application-specific configuration


class CollectionsAppConfig(AppConfig):
    # Configuration class for the 'collections_app' Django application
    default_auto_field = 'django.db.models.BigAutoField'
    # Specifies the default primary key type for models
    # in this app as BigAutoField
    name = 'collections_app'
    # Defines the name of the app, which must match the
    # folder name of the application
