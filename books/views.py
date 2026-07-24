from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Book


@login_required
def book_list(request):
    books = Book.objects.all().order_by('-added_on')
    return render(request, 'books/book_list.html', {'books': books})


def logout_view(request):
    logout(request)
    return redirect('login')
