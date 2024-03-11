from django.urls import path,re_path

from catalog.views import index,AuthorListView,AuthorDetailView,BookListView,BookListDetail

urlpatterns = [
    path("", index, name="index"),
    path("authors/", AuthorListView.as_view(), name="authors"),
    re_path(r"^authors/(?P<pk>\d+)/$", AuthorDetailView.as_view(), name="author-detail"),
    path("books/", BookListView.as_view(), name="books"),
    re_path(r"^books/(?P<pk>\d+)/$", BookListDetail.as_view(), name="book-detail"),
]
