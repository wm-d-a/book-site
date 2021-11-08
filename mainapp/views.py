from django.shortcuts import render
from .models import *


def main_page(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    context = {'books': books, 'genres': genres}
    return render(request, 'library/main_page.html', context)
