from django import forms
from .models import Journal

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'date', 'description', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }