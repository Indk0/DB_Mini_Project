from django.shortcuts import render
from .models import CollectorNotes, CustomerTransactions, PaymentPlans
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

# Create your views here.


def home(request):
    # View for the home page of the application
    # A context dictionary is defined to pass the title and welcome message 
    # to the template
    context = {
        'title': 'Home Page',
        'welcome_message': 'Welcome to the Collections Project!',
    }
    return render(request, 'collections_app/home.html')
# Render the 'home.html' template with the context data


def collectors_notes(request):
    # View for displaying collector notes
    notes = CollectorNotes.objects.all().order_by(
        '-created_at')
    # Fetch all collector notes from the database and sort them by creation
    # time in descending order
    context = {
        'title': 'Collectors Notes Page',
        'notes': notes,
    }
    return render(request, 'collections_app/collector_notes.html', context)
    # Render the 'collector_notes.html' template with the context data


def customer_transaction(request):
    # View for displaying customer transaction records
    transactions = CustomerTransactions.objects.all()
    # Fetch all customer transactions from the database
    context = {
        'title': 'Customer Transactions Page',
        'transactions': transactions,
    }
    return render(request, 'collections_app/customer_transaction.html',
                  context)
    # Render the 'customer_transaction.html' template with the context data


def plans(request):
    # View for displaying payment plans
    payment_plans = PaymentPlans.objects.all()
    # Fetch all payment plans from the database
    context = {
        'title': 'Payment Plans Page',
        'payment_plans': payment_plans,
    }
    return render(request, 'collections_app/payment_plans.html', context)
# Render the 'payment_plans.html' template with the context data


def edit_note(request):
    # View for handling the editing of a collector note
    if request.method == "POST":
        # Check if the request is a POST request
        note_content = request.POST.get("note_content")
        # Get the new note content from the POST data

        # Create a new CollectorNotes object with the provided content
        new_note = CollectorNotes(note=note_content)
        new_note.save()
        # Save the new note to the database

        # Redirect to the notes page after saving the note
        return redirect("notes")


def add_note(request):
    if request.method == "POST":
        # View for adding a new collector note
        collector_id = request.POST.get('collector_id')
        # Get the collector ID from the POST data
        note_content = request.POST.get('note_content')
        # Get the note content from the POST data

        if collector_id and note_content:
            # Ensure both collector ID and note content are provided
            CollectorNotes.objects.create(
                collector_id=collector_id, note=note_content)
            # Create a new note in the database with the provided data
            # Redirect to the collector notes page after adding the note
            return redirect('notes')

    # For GET requests or incomplete form submissions, render the
    # collector notes page
    return render(request, 'collections_app/collector_notes.html')
