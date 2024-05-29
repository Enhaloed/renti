from django.db.models import Q
from django.shortcuts import render

from .forms import SearchForm
from .models import Book, Author, Genre


def search_for_books(request):
    ctx = {}
    if request.method == 'GET':
        ctx['search_form'] = SearchForm()
    elif request.method == 'POST':
        ctx['is_search'] = True
        form = SearchForm(request.POST)
        if form.is_valid():
            search_text = form.cleaned_data['generic_text']
            if search_text:
                words = search_text.split(' ')
                #  Check that each word exists in any of the fields
                q = Q()
                for word in words:
                    word_q = Q()
                    for field in ['title', 'author__name', 'genre__name']:
                        #  Word is contained in any of the fields
                        word_q |= Q(**{f'{field}__icontains': word})

                    #  AND each word is accounted for
                    q &= word_q

                ctx['books'] = Book.objects.filter(q)

            else:
                ctx['books'] = Book.objects.all()

        ctx['search_form'] = form

    return render(request, 'book_club/html/search.html', context=ctx)