from django.contrib import admin

# Register your models here.
from .models import Company, User, Query

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Query)