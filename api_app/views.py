from django.shortcuts import render
from b2b_app.models import Query, CustomUser
from b2b_app.views import pretty_request, siteToSlug, slugToSite, Sort

# Create your views here.
from rest_framework import status

from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
import json
from checkmate_library.checkmate import get_book_site, Scribd, LivrariaCultura, GoogleBooks, TestBookstore, Kobo, Audiobooks
from checkmate_library.book_data import BookData, Format


example = {
    "email" : "b@gmail.com",
    "password" : "general", 
    "query" : {
        "title" : "Harry Potter", 
        "author" : "Suzanne Collins", 
        "ISBN" : ""
    }
}

class SearchAPI(APIView):

    def post(self, request, **kwargs):

        print(request.body)

        json_str = json.loads(request.body)

        user_email = json_str['email']
        password = json_str['password']

        user = CustomUser.objects.get(email=json_str['email'])

        if not user.check_password(password):
            return HttpResponse("Invalid login details supplied.")

        try:

            json_book_data = json_str['query']

            book_data = BookData()
            hasSearch = False
            if 'title' in json_book_data:
                if json_book_data['title'] != "":
                    book_data.title = json_book_data['title']
                    hasSearch = True
            if 'author' in json_book_data:
                json_book_data['author'] != ""
                if json_book_data['author'] != "":
                    book_data.authors = [json_book_data['author']]
                    hasSearch = True
            if 'ISBN' in json_book_data:
                if json_book_data['ISBN'] != "":
                    book_data.isbn_13 = json_book_data['ISBN']
                    hasSearch = True

            if not hasSearch:
                raise Exception()

        except: 
            return HttpResponse("Bad Request, Example: " + json.dumps(example))


        newQuery = Query()
        newQuery.user = user
        newQuery.save()

        book_data.print_data()
        company = user.getCompany()
        print(company)

        site_name_list = str(company.search_sites).split(",")
        site_slug_list = []
        site_list = []
        for site_name in site_name_list:
            Site = {"name": site_name, "slug": siteToSlug(site_name)}
            site_list.append(Site)
            site_slug_list.append(siteToSlug(site_name))

        result_data = {} 
        for site in site_slug_list:
            result_data[site] = [i for i in (Sort(get_book_site(site).find_book_matches(book_data))) if i[0] > .20]

        # test_book = BookData()
        # test_book.format = Format.DIGITAL
        # test_book.title = "Murder and Intrigue on the Mexican Border"
        # test_book.subtitle = "Somethign"
        # test_book.image_url = "https://books.google.com/books/content/images/frontcover/-lRoDwAAQBAJ?fif"
        # test_book.isbn_13 = "9781623495855"
        # test_book.authors = ['John A. Adams']
        # test_book.extra = {'Price': '$9.99'}

        # result_data = {'GB' : [(0.5, test_book), (0.5, test_book)]}

        for slug in result_data:
            book_list = result_data[slug]
            for count in range(0, len(book_list)): 
                book = book_list[count]  
                book[1].content = None
                book[1].image = None  
                book_list[count] = {'Match' : book[0], "Book" : book[1].data}
        
        return JsonResponse(result_data)

