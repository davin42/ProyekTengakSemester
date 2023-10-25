from django.shortcuts import render
from .models import Book

def beranda(request):
    books = Book.objects.all()

    # Implementasikan fitur filter di sini (gunakan request.GET untuk mendapatkan parameter filter)

    return render(request, 'beranda.html', {'books': books})
