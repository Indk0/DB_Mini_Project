from django.db import models

# Create your models here.
class CollectorNotes(models.Model):
    collector = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'collector'})
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note by {self.collector.username}"

class CustomerTransactions(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField()

    def __str__(self):
        return f"Transaction by {self.customer.username} - {self.amount}"

class PaymentPlans(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    plan_name = models.CharField(max_length=100)
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.IntegerField()

    def __str__(self):
        return f"Payment Plan for {self.customer.username}"
