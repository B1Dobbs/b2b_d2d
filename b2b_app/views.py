from django.shortcuts import render
from checkmate.book_data import bookData
from models import Company
import json

# Create your views here.

def searchView(request):

    if 'searchJSON' in request.GET:
        searchJSON = request.GET['searchJSON']
        book_data = json.loads(searchJSON)

    elif ('searchTitle' in request.GET) or ('searchAuthor' in request.GET) or ('searchISBN' in request.GET):
        book_data = bookData()
        if 'searchTitle' in request.GET:
            book_data.title = request.GET['searchTitle']
        if 'searchAuthor' in request.GET:
            book_data.author = request.GET['searchAuthor']
        if 'searchISBN' in request.GET:
            book_data.ISBN = request.GET['searchISBN']

    for site in Company.searchSites:
        data = get_book_site(site).get_site_specific_data(book_data)



        

