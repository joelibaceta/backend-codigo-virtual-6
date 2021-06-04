from catalog.models import Author, Book
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'view_author', 'editorial', 'year', 
        'price_in_usd')
    list_filter = ('editorial', 'author')

 
    def view_author(self, obj):

        if (obj.author != None):
            link = f"<a href='/admin/catalog/author/{obj.author.id}/change/'> {obj.author} </a>"
            return format_html(link)
        else:
            return "-"

    def price_in_usd(self, obj):
        if obj.price == None:
            f_price = 0.0
        else: 
            f_price = float(obj.price)
        return f"$ {f_price}"

admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)