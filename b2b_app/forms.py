from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models import Company, User
from django.http import HttpResponseRedirect


class CompanyForm(BSModalForm):

    class Meta:
        model = Company
        fields = ['name', 'contactPerson', 'contactNumber', 'searchSites', 'bookFormats']


class UserForm(BSModalForm):
   # company_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['name', 'email', 'password']


    


