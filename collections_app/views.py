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
    return HttpResponse("Collector Notes Page")


def customer_transaction(request):
    return HttpResponse("Customer Transactions Page")


def plans(request):
    return HttpResponse("Payment Plans Page")
