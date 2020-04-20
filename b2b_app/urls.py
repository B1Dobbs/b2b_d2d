from django.urls import path
from .views import CompanyListView, ReportingView

urlpatterns = [
    path('company-list/', CompanyListView.as_view(), name='company-list'),
    path('company-list/report/<int:pk>/', ReportingView.as_view(), name='report-view')
]
