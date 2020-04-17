from django.urls import path
from .views import CompanyListView, ReportingListView

urlpatterns = [
    path('company-list/', CompanyListView.as_view(), name='company-list'),
    path('company-list/report/<int:pk>/', ReportingListView.as_view(), name='report-list')
]
