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
from .forms import CompanyForm, CustomUserChangeForm, CustomUserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
import json
import sys
from django.http import HttpResponse
from django.template import loader
from .models import Company, CustomUser, Query
import datetime
from time import strptime

# pip install pandas
import pandas as pd
import sys
# pip install -i https://test.pypi.org/simple/ checkmate-library
from checkmate_library.checkmate import get_book_site, Scribd, LivrariaCultura, GoogleBooks, TestBookstore, Kobo, Audiobooks
from checkmate_library.book_data import BookData, Format, ParseStatus
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import RedirectView
from django.contrib.auth import logout, login
# Create your views here.


class Redirect(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'user_redirect'

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

def user_redirect(request):
    print(pretty_request(request))
    if request.user.is_superuser:
        return HttpResponseRedirect( reverse('company_list'))
    else: 
        return HttpResponseRedirect( reverse('search'))

class LogoutView(RedirectView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


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

class SearchCheckmateView(LoginRequiredMixin, View): #LoginRequiredMixin
    login_url = 'login'
    
    def get(self, request, **kwargs):
        company = request.user.getCompany()
        search = False
        site_list = []
        site_name_list = str(company.search_sites).split(",")
        print(site_name_list)
        for site_name in site_name_list:
            Site = {"name": site_name, "slug": siteToSlug(site_name)}
            site_list.append(Site)
    
        print(site_list)

        context = {
            'company' : company, 
            'site_list' : site_list,
        }
        return render(request, 'search_page.html', context)

    def post(self, request, **kwargs):
        company = request.user.getCompany()
        newQuery = Query()
        newQuery.user = request.user
        newQuery.save()

        if 'searchJSON' in request.POST:
            search = True
            searchJSON = request.POST['searchJSON']
            json_book_data = json.loads(searchJSON)
            print("Book Data:" + str(json_book_data))

            book_data = BookData()
            if 'title' in json_book_data:
                print("There's a title")
                book_data.title = json_book_data['title']
            if 'authors' in json_book_data:
                book_data.author = json_book_data['authors']
            if 'ISBN' in json_book_data:
                book_data.ISBN = json_book_data['ISBN']

            site_name_list = str(company.search_sites).split(",")
            site_slug_list = []
            site_list = []
            for site_name in site_name_list:
                Site = {"name": site_name, "slug": siteToSlug(site_name)}
                site_list.append(Site)
                site_slug_list.append(siteToSlug(site_name))

            result_data = {} 

            for site in site_slug_list:
                result_data[site] = [i for i in (Sort(get_book_site(site).find_book_matches(book_data))) if i[0] > .20]

            context = {
                'company': company,
                'searchResults': result_data,
                'site_list': site_list,
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
            

            site_name_list = str(company.search_sites).split(",")
            site_slug_list = []
            site_list = []
            for site_name in site_name_list:
                Site = {"name": site_name, "slug": siteToSlug(site_name)}
                site_list.append(Site)
                site_slug_list.append(siteToSlug(site_name))

            result_data = {} 

            for site in site_slug_list:
                result_data[site] = [i for i in (Sort(get_book_site(site).find_book_matches(book_data))) if i[0] > .20]
            
            print(result_data)

            context = {
                'company': company,
                'searchResults': result_data,
                'site_list': site_list,
                'search' : search,
            }

        return render(request, 'search_page.html', context)



class CompanyListView(SuperUserRequiredMixin, ListView):
    login_url = 'login'
    model = Company
    template_name = "company_list_page.html"
    company_list = Company.objects.all()
    paginate_by = 5
    company_list = Company.objects.all()

    def get_companies(self):
        context = {
            'company_list': company_list,
        }
        return context


class ReportingView(TemplateView):
    model = CustomUser
    template_name = "company_report.html"

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
            
                if int(query_count) != 0: 
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
        user_list = CustomUser.objects.filter(company = Company.objects.get(pk=self.kwargs['company_id']))
        context['company'] = Company.objects.get(pk = self.kwargs['company_id'])

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
        context['pk'] = self.kwargs['company_id']

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
        context['pk'] = self.kwargs['company_id']
        context['company'] = Company.objects.get(pk = self.kwargs['company_id'])
        return context


class CompanyCreateView(SuperUserRequiredMixin, BSModalCreateView):
    login_url = 'login'
    form_class = CompanyForm
    template_name = 'company/create_company.html'
    success_message = 'Success: Company was created.'
    success_url = reverse_lazy('company_list')

class CompanyUpdateView(SuperUserRequiredMixin, BSModalUpdateView):
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

class UserCreateView(SuperUserRequiredMixin, BSModalCreateView):
    login_url = 'login'
    form_class = CustomUserCreationForm
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
    def get(self, request, **kwargs):
        return super(UserCreateView, self).get(self, **kwargs)

class UserUpdateView(SuperUserRequiredMixin, BSModalUpdateView):
    login_url = 'login'
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'user/update_user.html'
    success_message = 'Success: User was updated.'

    def post(self, request, **kwargs):
        self.success_url = reverse('company_detail', kwargs={'pk':self.kwargs['company_id']})
        return super(UserUpdateView, self).post(request, **kwargs)


class UserDeleteView(SuperUserRequiredMixin, BSModalDeleteView):
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


