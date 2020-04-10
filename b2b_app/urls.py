from django.urls import path

from . import views

urlpatterns = [
    path('company/<int:pk>', views.CompanyDetailView.as_view(), name='company_detail'),
    #path('', views.CompanyListView.as_view(), name='company_list'),
    #path('company/create', views.CompanyCreateView.as_view(), name='create_company'),
    #path('company/update/<int:pk>', views.CompanyUpdateView.as_view(), name='update_company'),
    #path('company/delete/<int:pk>', views.CompanyDeleteView.as_view(), name='delete_book'),
    path('company/<int:company_id>/user/create', views.UserCreateView.as_view(), name='create_user'),
    path('company/<int:company_id>user/update/<int:pk>', views.UserUpdateView.as_view(), name='update_user'),
    path('company/<int:company_id>/user/delete/<int:pk>', views.UserDeleteView.as_view(), name='delete_user'),
]