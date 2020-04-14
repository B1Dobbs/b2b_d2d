from django.urls import path
from .views import HomePageView
from . import views

urlpatterns = [
    path('profile', views.profile_page, name='profile_page'),
    path('search', views.search_page, name='search_page'),
    path('', HomePageView.as_view(), name='home'),
    
    ]