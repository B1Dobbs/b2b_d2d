from django.shortcuts import render
from .models import Company, User, Query
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, ListView, TemplateView
from django import forms
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from django.urls import reverse_lazy
from .forms import CompanyForm, UserForm, UserChangeForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
import json
from checkmate_tool.book_data import BookData
import sys
from django.http import HttpResponse
from django.template import loader
'''from checkmate_tool.book_data import BookData
from checkmate_tool.checkmate import get_book_site, Scribd, LivrariaCultura, GoogleBooks, TestBookstore, Kobo
# Create your views here.

class SearchCheckmateView():
    
    def post(self, request, **kwargs):

        if 'searchJSON' in request.POST:
            searchJSON = request.POST['searchJSON']
            book_data = json.loads(searchJSON)

            result_data = []
            for site in Company.searchSites.choices:
                result_data[site] = get_book_site(site).find_book_matches(book_data)
                
            context = {
                'searchResults': result_data
            }
            return context

        elif ('searchTitle' in request.POST) or ('searchAuthor' in request.POST) or ('searchISBN' in request.POST):
            book_data = BookData()
            if 'searchTitle' in request.POST:
                book_data.title = request.POST['searchTitle']
            if 'searchAuthor' in request.POST:
                book_data.author = request.POST['searchAuthor']
            if 'searchISBN' in request.POST:
                book_data.ISBN = request.POST['searchISBN']

            result_data = []

            for site in Company.searchSites.choices:
                result_data[site] = get_book_site(site).find_book_matches(book_data)
            
            context = {
                'searchResults': result_data
            }

        return context
'''

class CompanyListView(ListView):
    model = Company
    template_name = "company_list_page.html"
    company_list = Company.objects.all()
    paginate_by = 5

    def get_companies(self):
        context = {
            'company_list': company_list,
        }
        return context

class CompanyCreateView(BSModalCreateView):
    form_class = CompanyForm
    template_name = 'company/create_company.html'
    success_message = 'Success: Company was created.'
    success_url = reverse_lazy('company_list')

class CompanyUpdateView(BSModalUpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/update_company.html'
    success_message = 'Success: Company was created.'

    def post(self, request, **kwargs):
        self.success_url = reverse('company_detail', kwargs={'pk':self.kwargs['pk']})
        return super(CompanyUpdateView, self).post(request, **kwargs)
        
class CompanyDetailView(DetailView):
    model = Company
    template = loader.get_template('company_detail.html')
    
    def get(self, request, *args, **kwargs):
        company = get_object_or_404(Company, pk=kwargs['pk'])
        users = User.objects.filter(company = kwargs['pk'])
        context = {'company': company, 'users' : users}
        return render(request, 'company_detail.html', context)

class UserCreateView(BSModalCreateView):
    form_class = UserForm
    template_name = 'user/create_user.html'
    success_message = 'Success: User was created.'

    def post(self, request, **kwargs):
        company_id = self.kwargs['company_id']
        self.success_url = reverse('company_detail', kwargs={'pk':company_id})
        self.company = Company.objects.get(pk=company_id)
        return super(UserCreateView, self).post(request, **kwargs)

    def form_valid(self, form):
        form.instance.company = self.company
        return super().form_valid(form)

class UserUpdateView(BSModalUpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/update_user.html'
    success_message = 'Success: User was updated.'

    def post(self, request, **kwargs):
        self.success_url = reverse('company_detail', kwargs={'pk':self.kwargs['company_id']})
        return super(UserUpdateView, self).post(request, **kwargs)


class UserDeleteView(BSModalDeleteView):
    model = User
    template_name = 'user/delete_user.html'
    success_message = 'Success: Book was deleted.'

    def post(self, request, **kwargs):
        self.success_url = reverse('company_detail', kwargs={'pk':self.kwargs['company_id']})
        return super(UserDeleteView, self).post(request, **kwargs)

'''For printing post requests if needed.'''
def pretty_request(request):
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1\n'
        'Content-Length: {content_length}\n'
        'Content-Type: {content_type}\n'
        '{headers}\n\n'
        '{body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    )



from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

def profile_page(request):
    template = loader.get_template('profile_page.html')
    company_name = "Helping Authors Inc."
    company_contact = "CatherineGates"
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
    search = True



    context = {
        'company_name': company_name,
        'company_contact': company_contact,
        'company_number': company_number,
        'user_list' : user_list,
        'site_list' : site_list,
        'bookFormat_list' : bookFormat_list,
        'search' : search,
    }
    return HttpResponse(template.render(context, request))

def search_page(request):
    template = loader.get_template('search_page.html')
    company_name = "Helping Authors Inc."
    company_contact = "Catherine Gates"
    company_number = "409-550-5500"
    site_list = [ 
        {"name": "Google Books",
         "slug": "GB",
        },
        {"name": "Scribd",
         "slug": "SD",
        },
        {"name": "Kobo",
         "slug": "KB",
        }]
    book_list = [
        {   "title": "Adventures of Sherlock Holmes GB1",
            "author": "Sir Arthur Conan Doyle",
            "format": "EBook",
            "match": "90%",
            "slug" : "GB",
        },
        {   "title": "Adventures of Sherlock Holmes KB1",
            "author": "Sir Arthur Conan Doyle",
            "format": "EBook",
            "match": "90%",
            "slug" : "KB",
        },
        {   "title": "Adventures of Sherlock Holmes SD",
            "author": "Sir Arthur Conan Doyle",
            "format": "EBook",
            "match": "90%",
            "slug" : "SD",
        },
        {   "title": "Adventures of Sherlock Holmes GB2",
            "author": "Sir Arthur Conan Doyle",
            "format": "EBook",
            "match": "90%",
            "slug" : "GB",
        },
        {   "title": "Adventures of Sherlock Holmes KB2",
            "author": "Sir Arthur Conan Doyle",
            "format": "EBook",
            "match": "90%",
            "slug" : "KB",
        },
    ]


    context = {
        'company_name': company_name,
        'company_contact': company_contact,
        'company_number': company_number,
        'site_list' : site_list,
        'book_list' : book_list,
    }
    return HttpResponse(template.render(context, request))

class HomePageView(TemplateView):
    template_name = 'home.html'