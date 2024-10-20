from django.urls import path

from .views import AuthorDetailView, AuthorListView, BookDetailView, BookListView

app_name = "libraries"

urlpatterns = [
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/<uuid:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<uuid:pk>/", BookDetailView.as_view(), name="book-detail"),
]
