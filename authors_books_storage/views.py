from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.db.models import Q
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)

from .forms import BookModelForm, AuthorModelForm

from .models import Book, Author
# <blog>/<modelname>_list.html

def index(request):
    return render(
        request,
        'main_page.html',
         context={},
    )

class BookListView(ListView):
    template_name = 'authors_books_storage/book_list.html'
    queryset = Book.objects.all()


class AuthorListView(ListView):
    template_name = 'authors_books_storage/author_list.html'
    queryset = Author.objects.all()

class BookDetailView(DetailView):
    template_name = 'authors_books_storage/book_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)

class AuthorDetailView(DetailView):
    template_name = 'authors_books_storage/author_detail.html'
    model = Author


@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    template_name = 'authors_books_storage/book_create.html'
    form_class = BookModelForm
    queryset = Book.objects.all() # <blog>/<modelname>_list.html
    page_name = "Add new book"

    def get_context_data(self, **kwargs):
        context = super(BookCreateView, self).get_context_data(**kwargs)
        context.update({'page_name': self.page_name})
        return context


@method_decorator(login_required, name='dispatch')
class BookUpdateView(UpdateView):
    template_name = 'authors_books_storage/book_create.html'
    model = Book
    fields = '__all__'
    page_name = "Edit book"

    def get_context_data(self, **kwargs):
        context = super(BookUpdateView, self).get_context_data(**kwargs)
        context.update({'page_name': self.page_name})
        return context

@method_decorator(login_required, name='dispatch')
class BookDeleteView(DeleteView):
    template_name = 'authors_books_storage/book_delete.html'

    model = Book
    fields = '__all__'

    def get_success_url(self):
        return reverse('book-list')




@method_decorator(login_required, name='dispatch')
class AuthorCreateView(CreateView):
    template_name = 'authors_books_storage/author_create.html'
    form_class = AuthorModelForm
    queryset = Author.objects.all() # <blog>/<modelname>_list.html
    page_name = "Add new author"

    def get_success_url(self):#success_url = '/'
        next_url = self.request.POST.get('next')  # here method should be GET or POST., None
        print(next_url)
        if next_url:
            return "%s" % (next_url)  # you can include some query strings as well
        else:
            return reverse('author-list')

    def get_context_data(self, **kwargs):
        context = super(AuthorCreateView, self).get_context_data(**kwargs)
        context.update({'page_name': self.page_name})
        return context


@method_decorator(login_required, name='dispatch')
class AuthorUpdateView(UpdateView):
    template_name = 'authors_books_storage/author_create.html'
    model = Author
    fields = '__all__'
    page_name = "Edit author"

    def get_context_data(self, **kwargs):
        context = super(AuthorUpdateView, self).get_context_data(**kwargs)
        context.update({'page_name': self.page_name})
        return context

@method_decorator(login_required, name='dispatch')
class AuthorDeleteView(DeleteView):
    template_name = 'authors_books_storage/author_delete.html'

    model = Author
    fields = '__all__'

    def get_success_url(self):
        return reverse('author-list')

class SearchResultsView(ListView):
    model = Book
    template_name = 'authors_books_storage/search_results.html'


class SearchResultsView(ListView):
    model = Book
    template_name = 'authors_books_storage/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Book.objects.filter(
                Q(title__icontains=query) | Q(author__name__icontains=query)
            ).distinct()
            return object_list


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'authors_books_storage/signup.html', {'form': form})

