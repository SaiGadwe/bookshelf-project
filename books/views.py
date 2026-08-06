from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from .forms import BookForm


@login_required
def book_list(request):
    all_books = Book.objects.all()
    books = all_books.order_by('-added_on')

    query = request.GET.get('q', '').strip()
    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))

    genre = request.GET.get('genre', '')
    if genre:
        books = books.filter(genre=genre)

    mine_only = request.GET.get('mine') == '1'
    if mine_only:
        books = books.filter(added_by=request.user)

    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    genre_counts = (
        all_books.values('genre').annotate(count=Count('id')).order_by('-count')
    )
    genre_label_map = dict(Book.GENRE_CHOICES)
    genre_stats = [
        {'label': genre_label_map.get(g['genre'], g['genre']), 'count': g['count']}
        for g in genre_counts
    ]

    context = {
        'page_obj': page_obj,
        'query': query,
        'selected_genre': genre,
        'genre_choices': Book.GENRE_CHOICES,
        'mine_only': mine_only,
        'total_books': all_books.count(),
        'genre_stats': genre_stats,
    }
    return render(request, 'books/book_list.html', context)


@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})


@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
