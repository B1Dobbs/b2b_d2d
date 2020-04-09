from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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

