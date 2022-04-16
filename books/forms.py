from django.forms import form
from django.forms.models import (
    inlineformset_factory,
    modelform_factory,
    modelformset_factory
    # these are all types of formsets we can use but i'd use the first import and keep the rest for remembrance
)
from .models import Book,Author




'''
Formsets in a Django is an advanced way of handling multiple forms on a single webpage. In other words, Formsets are a group of forms in Django. One might want to initialize multiple forms on a single page all of which may involve multiple POST requests
'''

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            "title",
            "number_of_pages"
        )

# holding shift and clicking on the inlineformset_factory would give you a number of items you can pass as arguments
BookFormSet = inlineformset_factory(
    parent_model=Author,
    model=Book,
    form=BookForm,
    min_num=2,
    extra=1,
)