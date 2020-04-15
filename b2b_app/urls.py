from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile_page, name='profile_page'),
    path('search', views.search_page, name='search_page'),
    path('companies', views.company_list_page, name='company_list_page'),
]
