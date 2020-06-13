from django.urls import path
from .views import (
                    BookListView,
                    AuthorListView,
                    index,
                    BookDetailView,
                    AuthorDetailView,
                    signup,
                    BookCreateView,
                    BookUpdateView,
                    BookDeleteView,
                    AuthorCreateView,
                    AuthorUpdateView,
                    AuthorDeleteView,
                    SearchResultsView,
                    )

# app_name = 'authors_books_storage'
urlpatterns = [
     path('', index, name='index'),
     path('signup/', signup, name='signup'),
     path('search/', SearchResultsView.as_view(), name='search_results'),

     path('books/', BookListView.as_view(), name='book-list'),
     path('book/<int:id>/', BookDetailView.as_view(), name='book-detail'),
     path('books/create/', BookCreateView.as_view(), name='book-create'),
     path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
     path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

     path('authors/', AuthorListView.as_view(), name='author-list'),
     path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
     path('authors/create/', AuthorCreateView.as_view(), name='author-create'),
     path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name='author-update'),
     path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
]