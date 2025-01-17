from django.shortcuts import render
from .models import CollectorNotes, CustomerTransactions, PaymentPlans
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

# Create your views here.


def home(request):
    # Context data can be passed to the template (if needed)
    context = {
        'title': 'Home Page',
        'welcome_message': 'Welcome to the Collections Project!',
    }
    return render(request, 'collections_app/home.html')


def collectors_notes(request):
    notes = CollectorNotes.objects.all().order_by(
        '-created_at')  # Sort by newest first
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
    return render(request, 'collections_app/customer_transaction.html',
                  context)


def plans(request):
    payment_plans = PaymentPlans.objects.all()
    context = {
        'title': 'Payment Plans Page',
        'payment_plans': payment_plans,
    }
    return render(request, 'collections_app/payment_plans.html', context)


def edit_note(request):
    if request.method == "POST":
        note_content = request.POST.get("note_content")

        # Create a new note
        new_note = CollectorNotes(note=note_content)
        new_note.save()

        return redirect("notes")  # Redirect back to the notes page


def add_note(request):
    if request.method == "POST":
        # Retrieve collector ID from the form
        collector_id = request.POST.get('collector_id')
        # Retrieve the note content from the form
        note_content = request.POST.get('note_content')

        if collector_id and note_content:
            # Save the data to the database
            CollectorNotes.objects.create(
                collector_id=collector_id, note=note_content)
            return redirect('notes')  # Redirect to the collector notes page

    # Handle GET requests or incomplete form submissions
    return render(request, 'collections_app/collector_notes.html')
