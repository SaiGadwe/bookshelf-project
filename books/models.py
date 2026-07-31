from django.db import models
from django.urls import reverse


class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('fantasy', 'Fantasy'),
        ('sci_fi', 'Science Fiction'),
        ('mystery', 'Mystery'),
        ('biography', 'Biography'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='other')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})
