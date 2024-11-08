from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.db.models import Q


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        if 'publisher' in request.POST:
            book.publisher = request.POST['publisher']
        if 'name' in request.POST:
            book.name = request.POST['name']
        if 'date' in request.POST and request.POST['date']:  # Check if the date field is not empty
            book.date = request.POST['date']
        if 'cost' in request.POST and request.POST['cost']:  # Check if the cost field is not empty
            book.cost = request.POST['cost']
        
        book.save()
        return redirect('book_list')

    return render(request, 'books/book_update.html', {'book': book})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

def book_search(request):
    query = request.GET.get('q')
    books = []

    if query:
        books = Book.objects.filter(
            Q(isbn__icontains=query) |
            Q(publisher__icontains=query) |
            Q(name__icontains=query)
        )

    context = {
        'books': books,
        'query': query,
    }
    return render(request, 'books/books_search.html', context)
