from django.shortcuts import render
from .models import Book  # Gantilah dengan model buku Anda

def beranda(request):
    # Ambil data buku dari basis data
    books = Book.objects.all()  # Mengambil semua buku, Anda bisa menambahkan filter sesuai kebutuhan

    # Implementasikan fitur filter di sini (gunakan request.GET untuk mendapatkan parameter filter)

    # Render halaman beranda dengan data buku
    return render(request, 'beranda.html', {'books': books})
