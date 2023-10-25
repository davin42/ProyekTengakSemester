from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'genre')
    list_filter = ('genre', 'published_date')
    search_fields = ('title', 'author')
