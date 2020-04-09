from django.shortcuts import render
from .models import Company, User
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django import forms
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from django.urls import reverse_lazy
from .forms import CompanyForm, UserForm, UserChangeForm

class CompanyListView(ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'index.html'

# Create your views here.
class CompanyDetailView(DetailView):
    model = Company
    template = loader.get_template('company/company_detail.html')
    
    def get(self, request, *args, **kwargs):
        pk =kwargs['pk']
        company = get_object_or_404(Company, pk=kwargs['pk'])
        users = User.objects.filter(company = pk)
        context = {'company': company, 'users' : users}
        return render(request, 'company_detail.html', context)

# #TODO
# class CompanyCreateView(DetailView):
    
#     template = loader.get_template('company_detail.html')
    
#     def get(self, request, *args, **kwargs):
#         pk =kwargs['pk']
#         company = get_object_or_404(Company, pk=kwargs['pk'])
#         users = User.objects.filter(company = pk)
#         context = {'company': company, 'users' : users}
#         return render(request, 'company_detail.html', context)


class UserCreateView(BSModalCreateView):
    print("CreateUser")
    form_class = UserForm
    template_name = 'user/create_user.html'
    success_message = 'Success: User was created.'
    success_url = reverse_lazy('company_detail')

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        request.POST['company_id'] = 1
        return super(UserCreateView, self).post(request, **kwargs)

class UserUpdateView(BSModalUpdateView):
    model = User
    template_name = 'user/update_user.html'
    form_class = UserChangeForm
    success_message = 'Success: User was updated.'
    success_url = reverse_lazy('company_detail')

