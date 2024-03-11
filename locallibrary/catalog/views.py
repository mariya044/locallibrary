from django.shortcuts import render
from catalog.models import Book,Author,BookInstance,Genre
from django.views.generic import ListView,DetailView


def index(request):
    num_books = Book.objects.all().count()
    num_author = Author.objects.all().count()
    num_book_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact="Available").count()

    return render(request, "index.html", {"num_books": num_books,
                                          "num_author": num_author,
                                          "num_book_instance": num_book_instance,
                                          "num_instance_available": num_instance_available})


# Create your views here.
class AuthorListView(ListView):
    model = Author
    template_name = "authors_list.html"
    context_object_name = "authors_list"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"


class BookListView(ListView):
    model=Book
    template_name="book_list.html"
    context_object_name = "books_list"


class BookListDetail(DetailView):
    model=Book
    template_name="book_detail.html"



