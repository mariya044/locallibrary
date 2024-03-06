from django.contrib import admin
from catalog.models import Author, Genre, Language, Book, BookInstance, Country


class BookInLine(admin.TabularInline):
    model = Book


class BookInstanceInline(admin.StackedInline):
    model = BookInstance



class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "pseudonym"]
    search_fields = ["pseudonym", "first_name", "last_name"]
    inlines=[BookInLine]


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "display_genre"]
    search_field = ["title","author__pseudonym","genre__name","author__first_name"]
    inlines = [BookInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ["book", "isbn", "status"]
    fieldset=(
        ("Group1",{
         "fields":("book","isbn","language")
        }),
        ("Group2",{
            "fields":("borrower","die_back","status")
        })
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
