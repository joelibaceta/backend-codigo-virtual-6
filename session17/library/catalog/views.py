
from catalog.models import Book
from django.shortcuts import render

def get_books_by_editorial(request, editorial):

    books = Book.objects.filter(editorial=editorial)

    year = request.GET.get("year")
    
    if year != None:
        books = books.filter(year=year)

    return render(request, 'catalog/index.html', {'books': books})

# Create your views here.
def catalog_list(request):
    books = Book.objects.all()
    return render(request, 'catalog/index.html', {'books': books})