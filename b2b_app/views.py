from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView

from .models import Company, User, Query

import datetime
from time import strptime

# pip install pandas
import pandas as pd

# Create your views here.
class CompanyListView(ListView):
    model = Company
    template_name = "company_list_view.html"
    paginate_by = 5
    company_list = Company.objects.all()


class ReportingView(TemplateView):
    model = User
    template_name = "reporting_view.html"

    def post(self, request, **kwargs):
        def get_date_list(self, first_m, first_y, second_m, second_y):
            """Get a list of all dates that allows us to easily query for reports

            Keyword arguments:
            self -- the instance of the class
            first_m -- the starting month of the report
            first_y -- the starting year of the report
            second_m -- the ending month of the report
            second_y -- the ending year of the report

            Returns:
            list -- list of all dates for the report
            """
            # Using datetime to convert short month name to int
            first_date = first_y + '-' + str(strptime(first_m, '%b').tm_mon) + '-01'
            second_date = second_y + '-' + str(strptime(second_m, '%b').tm_mon) + '-01'
            # Using pandas to convert the date range into a list of dates in format year-month
            date_list = pd.date_range(first_date, second_date, freq='MS',).strftime("%Y-%m").tolist()
            return date_list

        def get_total_queries(self, user_list, date_list):
            """Get a dictionary of the total queries for all months

            Keyword arguments:
            self -- the instance of the class
            user_list -- the list of all users in the company
            date_list -- the list of all dates for the report

            Returns:
            dictionary -- dictionary of users in format {user : [number of queries, percentage]}
            """
            user_total_queries_list = [] # List to hold queries for users
            total_query_count = 0 # Int to keep track of the total queries
            for users in user_list:
                query_count = 0 # Int to keep track of individual query total
                for month in date_list:
                    # Filtering for each month/year in list
                    query_num = Query.objects.filter(user = users, date__icontains = month).count()
                    query_count += query_num
                total_query_count += query_count
                # Adding the total query count to the list
                user_total_queries_list.append(query_count)

            user_dict = get_user_dict(self, user_list, user_total_queries_list, total_query_count)
            return user_dict

        def get_user_dict(self, user_list, user_queries_list, query_count):
            """Get a dictionary that holds the user, number of queries, and the percentage

            Keyword arguments:
            self -- the instance of the class
            user_list -- the list of all users in the company
            user_queries_list -- list of queries by user
            query_count -- total number of queries

            Returns:
            dictionary -- dictionary of users in format:
                          {user: [number of queries, percentage]}
            """
             # Create a dictionary to hold each user's queries and percentages
            total_company_percent = 0 # Add percentages to get total company percent
            user_dict = {} # Dictionary to hold the query number and percentages using the User as the key
            for users, queries in zip(user_list, user_queries_list):
                # If: there are queries then get the percentages
                # Else: set them to 0 queries to avoid errors
                if queries != '0': 
                    user_dict[users] = [queries, round((int(queries) / query_count) * 100)]
                    total_company_percent += round((int(queries) / query_count) * 100)
                else: 
                    user_dict[users] = [queries, 0]

            user_dict["Company Total"] = [query_count, total_company_percent]
            return user_dict

        def get_user_monthly_queries(self, date_list, user_list):
            """Get a dicitonary of user queries split by month

            Keyword arguments:
            self -- the instance of the class
            date_list -- the list of all dates for the report
            user_list -- the list of all users in the company

            Returns:
            dictionary -- dictionary of months in format:
                          {month name: {user: [number of queries, percentage]}}
            """
            month_split = {} # Dictionary to hold the user_dict per month 
            # Create a new entry in month_split for each possible month in the report
            for month in date_list:
                query_count = 0 # Int to keep track of the total queries
                user_queries_list = [] # List to hold queries for users
                for users in user_list:
                    query_num = Query.objects.filter(user = users, date__icontains = month).count()
                    query_count += query_num
                    user_queries_list += str(query_num)
                
                user_dict = get_user_dict(self, user_list, user_queries_list, query_count)

                format_month = month.split('-')
                # Format the months for long month name to display properly in template
                month_name = datetime.datetime.strptime(format_month[1].strip('0'), "%m").strftime("%B")
                month_split[month_name + ' ' + format_month[0]] = user_dict

            return month_split
  
        def get_possible_years(self):
            """Get a list of possible selectable years based on queries made

            Keyword arguments:
            self -- the instance of the class

            Returns:
            list -- possible years for dropdown box
            """
            # Get the possible years determined by the queries
            dates = Query.objects.filter().dates('date', 'month', order='DESC')
            possible_years = []
            for date in dates:
                if date.year not in possible_years:
                    possible_years.append(date.year)

            return possible_years

        context = super().get_context_data(**kwargs)

        # Get the post requests from the to and from dates
        first_m = self.request.POST['first_month']
        first_y = self.request.POST['first_year']
        second_m = self.request.POST['second_month']
        second_y = self.request.POST['second_year']
        
        # Get the total number of months between the two dates
        date_list = get_date_list(self, first_m, first_y, second_m, second_y)
        context['date_list'] = date_list
        
        # Create a list of users using the company pk that is passed in
        user_list = User.objects.filter(company = Company.objects.get(pk=self.kwargs['pk']))
        context['company'] = Company.objects.get(pk = self.kwargs['pk'])

        context['total_user_queries'] = get_total_queries(self, user_list, date_list)
        context['user_split'] = get_user_monthly_queries(self, date_list, user_list)
        context['year_list'] = get_possible_years(self)

        # Create a list of months to populate the dropdown box
        month_list = []
        for i in range(1,13):
            month_list.append(datetime.date(2020, i, 1).strftime('%b'))

        today = datetime.datetime.today()
        datem = datetime.datetime(today.year, today.month, 1)

        context['current_month'] = datem.strftime('%b')
        context['current_year'] = datem.year
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
        context['company'] = Company.objects.get(pk = self.kwargs['pk'])

        return context