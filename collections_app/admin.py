from django.contrib import admin
from .models import CollectorNotes, CustomerTransactions, PaymentPlans

# Register your models here.

admin.site.register(CollectorNotes)
admin.site.register(CustomerTransactions)
admin.site.register(PaymentPlans)