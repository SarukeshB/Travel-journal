# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import JournalForm
from .models import Journal

# View to add a new journal
def add_journal(request):
    if request.method == 'POST':
        form = JournalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_journals')  # Redirect to view journals page after adding
    else:
        form = JournalForm()
    return render(request, 'Travel/add_journal.html', {'form': form})

# View to display all journals
def view_journals(request):
    journals = Journal.objects.all()
    return render(request, 'Travel/view_journals.html', {'journals': journals})

# View to delete a journal
def delete_journal(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)

    # Only allow deletion via POST request
    if request.method == 'POST':
        journal.delete()
        return redirect('view_journals')  # Redirect back to the view journals page

    return redirect('view_journals')  # If not POST, redirect back to the view journals page
