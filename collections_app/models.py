from django.db import models

# Create your models here.


class CollectorNotes(models.Model):
    collector_id = models.IntegerField()
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerTransactions(models.Model):
    customer_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField()


class PaymentPlans(models.Model):
    customer_id = models.IntegerField()
    plan_name = models.CharField(max_length=100)
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.IntegerField()
