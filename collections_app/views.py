from django.shortcuts import render
from .models import CollectorNotes, CustomerTransactions, PaymentPlans
from django.http import HttpResponse

# Create your views here.


def home(request):
    # Context data can be passed to the template (if needed)
    context = {
        'title': 'Home Page',
        'welcome_message': 'Welcome to the Collections Project!',
    }
    return render(request, 'collections_app/home.html')


def collectors_notes(request):
    notes = CollectorNotes.objects.all()
    context = {
        'title': 'Collectors Notes Page',
        'notes': notes,
    }
    return render(request, 'collections_app/collector_notes.html', context)


def customer_transaction(request):
    transactions = CustomerTransactions.objects.all()
    context = {
        'title': 'Customer Transactions Page',
        'transactions': transactions,
    }
    return render(request, 'collections_app/customer_transaction.html', context)


def plans(request):
    context = {
        'title': 'Payment Plans Page',
    }
    return render(request, 'collections_app/payment_plans.html', context)
