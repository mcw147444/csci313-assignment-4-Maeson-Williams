from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    num_authors = Author.objects.count()
    
    num_genres = Genre.objects.filter(name__icontains='fiction').count()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_visits': num_visits
    }
    
    return render(request, 'index.html', context=context)

from django.views import generic

class AllLoanedBooksListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.can_mark_returned'
    permission_required = ('catalog.can_mark_returned', 'catalog.change_book')
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed.html'
    paginate_by = 10
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    
class BookDetailView(generic.DetailView):
    model = Book
    
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
    
class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
        )