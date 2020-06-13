from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Author(models.Model):
    name = models.CharField(max_length=100)
    #books = models.ManyToManyField('Book', related_name='books')

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)

    # author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.title}'



