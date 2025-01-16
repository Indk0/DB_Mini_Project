from django.contrib import admin
from .models import CollectorNotes, CustomerTransactions, PaymentPlans

# Register your models here.

# admin.site.register(CollectorNotes)
admin.site.register(CustomerTransactions)
admin.site.register(PaymentPlans)

@admin.register(CollectorNotes)
class CollectorNotesAdmin(admin.ModelAdmin):
    list_display = ('collector_id', 'note', 'created_at', 'updated_at')  # Show these columns
    search_fields = ('collector_id', 'note')  # Allow search by collector ID and note
    list_filter = ('created_at',)  # Add a filter by creation date