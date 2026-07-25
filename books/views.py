from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm


@login_required
def book_list(request):
    books = Book.objects.all().order_by('-added_on')
    return render(request, 'books/book_list.html', {'books': books})


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
