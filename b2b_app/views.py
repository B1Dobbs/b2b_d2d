from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView

from .models import Company, User, Query

import datetime
from time import strptime
# Create your views here.

class CompanyListView(ListView):
    model = Company
    template_name = "company_list_view.html"
    paginate_by = 5
    company_list = Company.objects.all()


class ReportingListView(TemplateView):
    model = User
    template_name = "reporting_list_view.html"

    def post(self, request, **kwargs):
        # Get the post request for the to and from dates
        first_m = self.request.POST['first_month']
        first_y = self.request.POST['first_year']
        second_m = self.request.POST['second_month']
        second_y = self.request.POST['second_year']
        
        # Create a dictionary to easily get the number associated with each short month name
        months = { 'Jan' : '01', 'Feb' : '02', 'Mar' : '03', 'Apr' : '04',
            'May' : '05', 'Jun' : '06', 'Jul' : '07', 'Aug' : '08', 'Sep' : '09',
            'Oct' : '10', 'Nov' : '11', 'Dec' : '12'}
        
        # Get the total number of months between the two dates
        start_date = datetime.datetime(int(first_y), strptime(first_m, '%b').tm_mon, 1)
        end_date = datetime.datetime(int(second_y), strptime(second_m, '%b').tm_mon, 1)
        num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

        context = super().get_context_data(**kwargs)

        context['total_months'] = num_months

        # Create a list of users using the company pk that is passed in
        user_list = User.objects.filter(company = Company.objects.get(pk=self.kwargs['pk']))
        context['company'] = Company.objects.get(pk = self.kwargs['pk'])

        # Set each users query count per month
        query_count = 0
        user_queries_list = []
        for users in user_list:
            query_num = Query.objects.filter(user = users, date__icontains = '2020-04').count()
            query_count += query_num
            user_queries_list += str(query_num)

        # Create a dictionary to hold each user's queries and percentages
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

        # Get the possible years determined by the queries
        dates = Query.objects.filter().dates('date', 'month', order='DESC')
        possible_years = []
        for date in dates:
            if date.year not in possible_years:
                possible_years.append(date.year)

        # Create a list of months to populate the dropdown box
        month_list = []
        for i in range(1,13):
            month_list.append(datetime.date(2020, i, 1).strftime('%b'))

        today = datetime.datetime.today()
        datem = datetime.datetime(today.year, today.month, 1)

        context['current_month'] = datem.strftime('%b')
        context['current_year'] = datem.year
        context['year_list'] = possible_years
        context['month_list'] = month_list

        context['pk'] = self.kwargs['pk']

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
        context['pk'] = self.kwargs['pk']

        return context