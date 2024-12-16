# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_journal, name='add_journal'),  # URL for adding a journal
    path('view/', views.view_journals, name='view_journals'),  # URL for viewing all journals
    path('delete/<int:journal_id>/', views.delete_journal, name='delete_journal'),  # URL for deleting a journal
]
