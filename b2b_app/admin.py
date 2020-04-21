from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
from .models import Company, CustomUser, Query

admin.site.register(Company)
admin.site.register(CustomUser)
admin.site.register(Query)
