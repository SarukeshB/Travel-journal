from django.shortcuts import render, redirect, get_object_or_404
from .forms import JournalForm
from .models import Journal

def add_journal(request):
    try:
        if request.method == 'POST':
            form = JournalForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('view_journals')
        else:
            form = JournalForm()
        return render(request, 'Travel/add_journal.html', {'form': form})
    except Exception as e:
        return render(request, 'Travel/error.html', {'error': str(e)})

def view_journals(request):
    try:
        journals = Journal.objects.all()
        return render(request, 'Travel/view_journals.html', {'journals': journals})
    except Exception as e:
        return render(request, 'Travel/error.html', {'error': str(e)})

def delete_journal(request, journal_id):
    try:
        journal = get_object_or_404(Journal, id=journal_id)

        if request.method == 'POST':
            journal.delete()
            return redirect('view_journals')
        return redirect('view_journals')
    except Exception as e:
        return render(request, 'Travel/error.html', {'error': str(e)})
