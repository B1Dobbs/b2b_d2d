from django.shortcuts import render
from django.core.paginator import Paginator

from django.views.generic import TemplateView, ListView

from .models import Company, User, Query

import datetime
# Create your views here.

class CompanyListView(ListView):
    model = Company
    template_name = "company_list_view.html"
    paginate_by = 5
    company_list = Company.objects.all()


class ReportingListView(ListView):
    model = User
    template_name = "reporting_list_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_list = User.objects.filter(company = Company.objects.get(pk=self.kwargs['pk']))
        context['company'] = Company.objects.get(pk = self.kwargs['pk'])

        query_count = 0
        user_queries_list = []
        for users in user_list:
            query_num = Query.objects.filter(user = users, date__icontains = '2020-04').count()
            query_count += query_num
            user_queries_list += str(query_num)

        total_company_percent = 0
        user_dict = {}
        for users, queries in zip(user_list, user_queries_list):
            if queries != '0':
                user_dict[users] = [queries, round((int(queries) / query_count) * 100)]
                total_company_percent += round((int(queries) / query_count) * 100)
            else:
                user_dict[users] = [queries, 0]

        user_dict["Company Total"] = [query_count, total_company_percent]
        context['user_dict'] = user_dict

        dates = Query.objects.filter().dates('date', 'month', order='DESC')
        possible_years = []
        for date in dates:
            if date.year not in possible_years:
                possible_years.append(date.year)

        month_list = []
        for i in range(1,13):
            month_list.append(datetime.date(2020, i, 1).strftime('%b'))

        today = datetime.datetime.today()
        datem = datetime.datetime(today.year, today.month, 1)

        context['current_month'] = datem.strftime('%b')
        context['current_year'] = datem.year
        context['year_list'] = possible_years
        context['month_list'] = month_list

        return context