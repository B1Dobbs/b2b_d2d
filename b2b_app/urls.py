from django.urls import path
from .views import CompanyListView

urlpatterns = [
    path('company-list/', CompanyListView.as_view(), name='company-list'),
]
