from django.shortcuts import render, redirect
from .forms import BookForm
from books.models import Books
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from books.models import User


# Create your views here.
def list_books(request):
    books = Books.objects.all().order_by("title")
    user = User.objects.get(id=request.user.id)
    favorites = user.favorite_books.all()
    return render(request, "books/list_books.html", {"books": books, "favorites": favorites})

def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')
    return render(request, "books/add_book.html", {"form": form})

def add_favorite(request, pk):
    book = Books.objects.get(id=pk)
    user = User.objects.get(id=request.user.id)
    user.favorite_books.add(book)
    return HttpResponseRedirect('/')

def remove_favorite(request, pk):
    book = Books.objects.get(id=pk)
    user = User.objects.get(id=request.user.id)
    user.favorite_books.remove(book)
    return HttpResponseRedirect('/')