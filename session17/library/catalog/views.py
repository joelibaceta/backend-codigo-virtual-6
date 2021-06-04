
from catalog.models import Author, Book
from django.shortcuts import redirect, render
from catalog.forms import ModelBookForm
from django.views.generic.edit import CreateView, UpdateView

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

def update_book(request, pk):
    if request.method == 'POST':
        
        data = request.POST

        author = Author.objects.get(pk=data['author'])

        book = Book.objects.get(pk=pk)
        book.title = data['title']
        book.author = author
        book.editorial = data['editorial']
        book.year = data['year']
        book.volume = data['volume']
        book.save()

        return redirect('/catalog')

    else:
        book = Book.objects.get(pk=pk)
        form = ModelBookForm(book.__dict__)
        return render(request, 'catalog/new.html', {"form": form})


def new_book(request):
    if request.method == 'POST':
        data = request.POST

        book = Book()
        book.title = data['title']
        #book.autor = data['autor']
        book.editorial = data['editorial']
        book.year = data['year']
        book.volume = data['volume']
        book.save()

        return redirect('/catalog')
        
    else:
        form = ModelBookForm()
        return render(request, 'catalog/new.html', {"form": form})

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