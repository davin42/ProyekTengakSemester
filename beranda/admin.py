from django.contrib import admin
from .models import Book  # Gantilah dengan model buku Anda

# Daftarkan model buku di admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'genre')  # Atur bidang yang ingin ditampilkan di daftar admin
    list_filter = ('genre', 'published_date')  # Filter data berdasarkan genre dan tanggal terbit
    search_fields = ('title', 'author')  # Tambahkan bidang pencarian

# Jika Anda ingin mengelola model lain dalam modul "Beranda," Anda juga bisa mendaftarkannya di sini.
