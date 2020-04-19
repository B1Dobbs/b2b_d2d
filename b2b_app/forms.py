from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models import Company, User
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CompanyForm(BSModalForm):

    class Meta:
        model = Company
        fields = ['name', 'contact_person', 'contact_number', 'search_sites', 'book_formats']


class UserForm(BSModalForm):
   # company_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'company', 'active')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'company', 'active')
