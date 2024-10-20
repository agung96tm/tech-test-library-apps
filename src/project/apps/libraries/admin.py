from apps.libraries.models import Author, Book
from django.contrib import admin


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "bio")
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ("title", "author__name")
