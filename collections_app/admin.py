from django.contrib import admin
from .models import CollectorNotes, CustomerTransactions, PaymentPlans

# Import the admin module from Django and the models to be registered
# in the admin interface

# Register your models here.

# Register the CustomerTransactions and PaymentPlans models
# with default admin settings
admin.site.register(CustomerTransactions)
admin.site.register(PaymentPlans)

# Use the @admin.register decorator to register the CollectorNotes model
# with custom admin configurations


@admin.register(CollectorNotes)
class CollectorNotesAdmin(admin.ModelAdmin):
    # Custom admin configuration for the CollectorNotes model
    list_display = ('collector_id', 'note', 'created_at',
                    'updated_at')  # Specify the fields to display admin list
    search_fields = ('collector_id', 'note')
    # Add a search box to the admin interface to allow searching by
    # collector ID or note content
    list_filter = ('created_at',)
    # Add a filter sidebar in the admin interface for filtering
    # by the created_at field