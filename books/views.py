from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Author,Book
from .forms import BookFormSet

# Create your views here.

def create_book(request,pk):
    author = Author.objects.get(pk=pk)
    # pass the request.POST or none
    formset = BookFormSet(request.POST or None)

    if request.method == 'POST':
        if formset.is_valid():
            # assigning the instance thus the item of info typical to the class formset to author
            formset.instance = author
            formset.save()
            return redirect("create-book",pk=author.id)

    context = {
        "formset":formset
    }
    return render(request,"create_book.html",context)
