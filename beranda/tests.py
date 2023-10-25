from django.test import TestCase
from .models import Book

class BerandaTests(TestCase):
    def setUp(self):
        # Persiapan data tes, contohnya:
        Book.objects.create(title='Judul Buku 1', author='Penulis 1', published_date='2023-10-25', genre='Fiksi')
        Book.objects.create(title='Judul Buku 2', author='Penulis 2', published_date='2023-10-26', genre='Non-Fiksi')

    def test_buku_ditampilkan_pada_beranda(self):
        response = self.client.get('/beranda/')  # Ganti dengan URL yang sesuai
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['books'], ['<Book: Judul Buku 1>', '<Book: Judul Buku 2>'])
      
