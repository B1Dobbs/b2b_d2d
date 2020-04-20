from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.core.paginator import *
from .models import Company, Query
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, ListView, TemplateView
from django import forms
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from django.urls import reverse_lazy
from .forms import CompanyForm, UserForm, UserChangeForm, CustomUserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import CustomUser

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




# Create your views here.

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
        users = CustomUser.objects.filter(company = kwargs['pk'])
        context = {'company': company, 'users' : users}
        return render(request, 'company_detail.html', context)

class UserCreateView(BSModalCreateView):
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

class UserUpdateView(BSModalUpdateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'user/update_user.html'
    success_message = 'Success: User was updated.'

    def post(self, request, **kwargs):
        self.success_url = reverse('company_detail', kwargs={'pk':self.kwargs['company_id']})
        return super(UserUpdateView, self).post(request, **kwargs)


class UserDeleteView(BSModalDeleteView):
    model = CustomUser
    template_name = 'user/delete_user.html'
    success_message = 'Success: Book was deleted.'

    def post(self, request, **kwargs):
        self.success_url = reverse('company_detail', kwargs={'pk':self.kwargs['company_id']})
        return super(UserDeleteView, self).post(request, **kwargs)

'''For printing post requests if needed. '''
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

class HomePageView(TemplateView):
    template_name = 'home.html'