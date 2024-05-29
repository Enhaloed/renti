from django.shortcuts import render

from .forms import SearchForm


def search_for_books(request):
    ctx = {}
    if request.method == 'GET':
        ctx['search_form'] = SearchForm()
    elif request.method == 'POST':
        form = SearchForm(request.user, request.POST)

    return render(request, 'book_club/html/search.html', context=ctx)