from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="countries"


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    pseudonym = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}{self.last_name}{self.pseudonym}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)  # promezytochnaya table net in our table

    def display_genre(self):
        return ",".join([genre.name for genre in self.genre.all()])

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    STATUSES = (
        ("Available", "Available"),
        ("On Loan", "On Loan"),
        ("Lost", "Lost"),
        ("On service", "On service")
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, max_length=50, default="Available")
    due_back = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title}{self.isbn}"

