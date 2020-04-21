from django import forms
from .models import CustomUser
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models import Company, CustomUser
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

class CompanyForm(BSModalForm):

    class Meta:
        model = Company
        fields = ['name', 'contact_person', 'contact_number', 'search_sites', 'book_formats']

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')