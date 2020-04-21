from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, ListView, TemplateView, View
from django import forms
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from django.urls import reverse_lazy
from .forms import CompanyForm, UserForm, UserChangeForm, CustomUserChangeForm, CustomUserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
import json
import sys
from django.http import HttpResponse
from django.template import loader
from .models import Company, CustomUser, Query
import sys
#from checkmate_library.checkmate import get_book_site, Scribd, LivrariaCultura, GoogleBooks, TestBookstore, Kobo, Audiobooks
#from checkmate_library.book_data import BookData, Format, ParseStatus
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def Sort(tup): #sort 
    return(sorted(tup, key = lambda x: float(x[0]), reverse = True))

def siteToSlug(site):
    if "Test Bookstore" in site:
        return "TB"
    elif "Google Books" in site:
        return "GB"
    elif "Kobo" in site:
        return "KB"
    elif "Livraria Cultura" in site:
        return "LC"
    elif "Audiobooks" in site:
        return "AB"
    elif "Scribd" in site:
        return "SD"

def slugToSite(site):
    if site == "TB":
        return "Test Bookstore"
    elif site == "GB":
        return " Google Books"
    elif site == "KB":
        return " Kobo"
    elif site == "LC":
        return "Livraria Cultura"
    elif site =="AB":
        return "Audiobooks"
    elif site =="SD":
        return "Scribd"

class SearchCheckmateView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self, request, **kwargs):
        search = False
        company_name = "Helping Authors Inc."
        company_contact = "Catherine Gates"
        company_number = "409-550-5500"
        site_list = []
        site_name_list = str(request.user.getCompany().search_sites).split(",")
        print(site_name_list)
        for site_name in site_name_list:
            Site = {"name": site_name, "slug": siteToSlug(site_name)}
            site_list.append(Site)
    
        print(site_list)

        context = {
            'company_name': company_name,
            'company_contact': company_contact,
            'company_number': company_number,
            'site_list' : site_list,
        }
        return render(request, 'search_page.html', context)

    def post(self, request, **kwargs):

        if 'searchJSON' in request.POST:
            search = True
            searchJSON = request.POST['searchJSON']
            book_data = json.loads(searchJSON)
            print("Book Data:" + str(book_data))

            result_data = []
            #for site in Company.search_sites.choices:
                #result_data[site] = get_book_site(site).find_book_matches(book_data)
                
            context = {
                'searchResults': result_data,
                'search' : search,
            }
            

        elif ('searchTitle' in request.POST) or ('searchAuthor' in request.POST) or ('searchISBN' in request.POST):
            search = True
            book_data = BookData()
            if 'searchTitle' in request.POST:
                book_data.title = request.POST['searchTitle']
            if 'searchAuthor' in request.POST:
                book_data.author = request.POST['searchAuthor']
            if 'searchISBN' in request.POST:
                book_data.ISBN = request.POST['searchISBN']
            
            site_name_list = str(request.user.getCompany().search_sites).split(",")
            site_slug_list = []
            site_list = []
            for site_name in site_name_list:
                Site = {"name": site_name, "slug": siteToSlug(site_name)}
                site_list.append(Site)
                site_slug_list.append(siteToSlug(site_name))
    
            print(site_slug_list)

            result_data = {} 

            #for site in site_slug_list:
                #result_data[site] = [i for i in (Sort(get_book_site(site).find_book_matches(book_data))) if i[0] > .20]
            
            print(result_data)

            context = {
                'searchResults': result_data,
                'site_list': site_list,
                'search' : search,
            }

        return render(request, 'search_page.html', context)


class CompanyListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Company
    template_name = "company_list_page.html"
    company_list = Company.objects.all()
    paginate_by = 5

    def get_companies(self):
        context = {
            'company_list': company_list,
        }
        return context

class CompanyCreateView(LoginRequiredMixin, BSModalCreateView):
    login_url = 'login'
    form_class = CompanyForm
    template_name = 'company/create_company.html'
    success_message = 'Success: Company was created.'
    success_url = reverse_lazy('company_list')

class CompanyUpdateView(LoginRequiredMixin, BSModalUpdateView):
    login_url = 'login'
    model = Company
    form_class = CompanyForm
    template_name = 'company/update_company.html'
    success_message = 'Success: Company was created.'

    def post(self, request, **kwargs):
        self.success_url = reverse('company_detail', kwargs={'pk':self.kwargs['pk']})
        return super(CompanyUpdateView, self).post(request, **kwargs)
        
class CompanyDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Company
    template = loader.get_template('company_detail.html')
    def get(self, request, *args, **kwargs):
        company = get_object_or_404(Company, pk=kwargs['pk'])
        users = CustomUser.objects.filter(company = kwargs['pk'])
        context = {'company': company, 'users' : users}
        return render(request, 'company_detail.html', context)

class UserCreateView(LoginRequiredMixin, BSModalCreateView):
    login_url = 'login'
    form_class = CustomUserCreationForm
    template_name = 'user/create_user.html'
    success_message = 'Success: User was created.'

    def post(self, request, **kwargs):
        company_id = self.kwargs['company_id']
        self.success_url = reverse('company_detail', kwargs={'pk':company_id})
        self.company = Company.objects.get(pk=company_id)
        print(self)
        return super(UserCreateView, self).post(request, **kwargs)

    def form_valid(self, form):
        form.instance.company = self.company
        return super().form_valid(form)
    def get(self, request, **kwargs):
        return super(UserCreateView, self).get(self, **kwargs)

class UserUpdateView(LoginRequiredMixin, BSModalUpdateView):
    login_url = 'login'
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'user/update_user.html'
    success_message = 'Success: User was updated.'

    def post(self, request, **kwargs):
        self.success_url = reverse('company_detail', kwargs={'pk':self.kwargs['company_id']})
        return super(UserUpdateView, self).post(request, **kwargs)


class UserDeleteView(LoginRequiredMixin, BSModalDeleteView):
    login_url = 'login'
    model = CustomUser
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


class LoginView(TemplateView):
    template_name = 'login.html'
