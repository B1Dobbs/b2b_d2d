from django.shortcuts import render
from django.core.paginator import Paginator

from django.views.generic import TemplateView, ListView

from .models import Company, User, Query
# Create your views here.

class CompanyListView(ListView):
    model = Company
    template_name = "company_list_view.html"
    company_list = Company.objects.all()
    paginate_by = 5

    def get_companies(self):
        context = {
            'company_list': company_list,
        }
        return context