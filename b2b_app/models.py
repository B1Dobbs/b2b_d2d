from django.db import models
from django.contrib.auth.models import AbstractUser

# pip install django-multiselectfield
from multiselectfield import MultiSelectField

# Create your models here.
class Company(models.Model):
    SITE_CHOICES = (
        ('TB', 'Test Bookstore'),
        ('GB', 'Google Books'),
        ('KB', 'Kobo'),
        ('LC', 'Livraria Cultura'),
        ('SD', 'Scribd'),
    )
    BOOK_FORMATS = (
        ('EBook', 'EBook'),
        ('Audio Book', 'Audio Book'),
        ('Print Book', 'Print Book'),
    )
    name = models.CharField(max_length=250)
    contactPerson = models.CharField(max_length = 250)
    contactNumber = models.CharField(max_length = 12)
    searchSites = MultiSelectField(max_length = 100, choices = SITE_CHOICES)
    bookFormats = MultiSelectField(max_length = 100, choices = BOOK_FORMATS)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    # add additional fields in here
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null = True)
    def __str__(self):
        return self.email

'''
class User(models.Model):
    name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 250)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    password = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
'''

class Query(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.user.name + " (" + str(self.date) + ")"
