from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Author,Book
from .forms import BookFormSet,BookForm

# Create your views here.

def create_book(request,pk):
    author = Author.objects.get(pk=pk)
    # pass the request.POST or none
    form = BookForm(request.POST or None)
    books = Book.objects.filter(author=author)

    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            # assigning the instance thus the item of info typical to the class formset to author
            book.author = author
            book.save()
            return redirect("detail-book",pk=book.id)
        else:
            # this should run when there are errors in the form the form should be resubmitted
            return render(request,"partials/bookform.html",{"form":form})

    context = {
        "form":form,
        "author":author,
        "books":books
    }
    return render(request,"create_book.html",context)


def create_book_form(request):
    form = BookForm()
    context = {
        "form": form
    }
    return render(request,'partials/bookform.html',context)

def update_book(request,pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None,instance=book)
    if request.method == 'POST':
        if form.is_valid():
            book = form.save()
            return redirect("detail-book",pk=book.id)
    context = {
        "form": form,
        "book":book 
    }
    return render(request,'partials/bookform.html',context)


def detail_book(request,pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book
    }
    return render(request,'partials/book_detail.html',context)

def delete_book(request,pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse('')
