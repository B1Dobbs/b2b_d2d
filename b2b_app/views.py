from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import *

def profile_page(request):
    template = loader.get_template('profile_page.html')
    company_name = "Helping Authors Inc."
    company_contact = "Catherine Gates"
    company_number = "409-550-5500"
    user_list = [
        {   "name": "Catherine Gates",
            "email": "catherine.gates@email.com",
        },
        {   "name": "Brooke Dobbins",
            "email": "brooke.dobbins@email.com",
        },
        {   "name": "Nathan Schrader",
            "email": "nathan.schrader@email.com",
        },
        {   "name": "Trevor Bailey",
            "email": "trevor.bailey@email.com",
        },
        {   "name": "Tyler Matthews",
            "email": "tyler.matthews@email.com",
        },
    ]

    site_list = [ "Google Books", "Scribd", "Kobo"]
    bookFormat_list = ["EBook", "Print"]



    context = {
        'company_name': company_name,
        'company_contact': company_contact,
        'company_number': company_number,
        'user_list' : user_list,
        'site_list' : site_list,
        'bookFormat_list' : bookFormat_list,
    }
    return HttpResponse(template.render(context, request))

def search_page(request):
    template = loader.get_template('search_page.html')
    company_name = "Helping Authors Inc."
    company_contact = "Catherine Gates"
    company_number = "409-550-5500"
    user_list = [
        {   "name": "Catherine Gates",
            "email": "catherine.gates@email.com",
        },
        {   "name": "Brooke Dobbins",
            "email": "brooke.dobbins@email.com",
        },
        {   "name": "Nathan Schrader",
            "email": "nathan.schrader@email.com",
        },
        {   "name": "Trevor Bailey",
            "email": "trevor.bailey@email.com",
        },
        {   "name": "Tyler Matthews",
            "email": "tyler.matthews@email.com",
        },
    ]


    context = {
        'company_name': company_name,
        'company_contact': company_contact,
        'company_number': company_number,
        'user_list' : user_list,
    }
    return HttpResponse(template.render(context, request))


class CompanyListView(ListView):
    model = Company
    template_name = "company_list_page.html"
    company_list = Company.objects.all()
    paginator = Paginator(company_list, 5)
    page = request.GET.get('page', '1')
    company_list = paginator.get_page(page)

    def get_companies(self):
        context = {
            'company_list': company_list,
            'page' : page
        }
        return context


# def company_list_page(request):
#     template = loader.get_template('company_list_page.html')

#     company_list = [
#         {
#             "company_name": "Helping Authors Inc.",
#             "contact_number": "911",
#         },
#         {
#             "company_name": "The Unhelpful Authors Inc.",
#             "contact_number": "119",
#         },
#         {
#             "company_name": "The Averagely Helpful Authors Inc.",
#             "contact_number": "191",
#         },
#         {
#             "company_name": "Helping Authors Inc.",
#             "contact_number": "911",
#         },
#         {
#             "company_name": "The Unhelpful Authors Inc.",
#             "contact_number": "119",
#         },
#         {
#             "company_name": "The Averagely Helpful Authors Inc.",
#             "contact_number": "191",
#         },
#     ]

#     # Paginate the list
#     paginator = Paginator(company_list, 5)
#     page = request.GET.get('page', '1')
#     company_list = paginator.get_page(page)
#     context = {
#         'company_list' : company_list,
#         'page': page,
#     }

    # return HttpResponse(template.render(context,request))

