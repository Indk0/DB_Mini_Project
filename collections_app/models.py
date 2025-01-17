from django.db import models

# Import the models module from Django to define database models


class CollectorNotes(models.Model):
    # Model to represent notes added by collectors
    collector_id = models.IntegerField()
    # ID of the collector associated with the note
    note = models.TextField()
    # Content of the note, stored as text
    created_at = models.DateTimeField(auto_now_add=True)
    # Timestamp indicating when the note was created (auto-generated)
    updated_at = models.DateTimeField(auto_now=True)
    # Timestamp indicating the last update of the note (auto-updated)

    class Meta:
        verbose_name_plural = "collector notes"
        # Sets the plural name for the model in the admin interface


class CustomerTransactions(models.Model):
    # Model to represent customer transactions
    customer_id = models.IntegerField()
    # ID of the customer associated with the transaction
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Transaction amount with a maximum of 10 digits and 2 decimal places
    transaction_date = models.DateTimeField()
    # Date and time of the transaction

    class Meta:
        verbose_name_plural = "customer transactions"
        # Sets the plural name for the model in the admin interface


class PaymentPlans(models.Model):
    # Model to represent payment plans for customers
    customer_id = models.IntegerField()
    # ID of the customer associated with the payment plan
    plan_name = models.CharField(max_length=100)
    # Name of the payment plan with a maximum length of 100 characters
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)
    # Monthly payment amount with a maximum of 10 digits and 2 decimal places
    duration_months = models.IntegerField()
    # Duration of the payment plan in months

    class Meta:
        verbose_name_plural = "payment plans"
        # Sets the plural name for the model in the admin interface
