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
        ('AB', 'Audiobooks')
    )
    BOOK_FORMATS = (
        ('EBook', 'EBook'),
        ('Audio Book', 'Audio Book'),
        ('Print Book', 'Print Book'),
    )
    name = models.CharField(max_length=250)
    contact_person = models.CharField(max_length = 250)
    contact_number = models.CharField(max_length = 12)
    #Having blank on these two allows to avoid form validation on these fields
    search_sites = MultiSelectField(max_length = 100, choices = SITE_CHOICES, blank=True)
    book_formats = MultiSelectField(max_length = 100, choices = BOOK_FORMATS, blank=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    # add additional fields in here
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null = True)
    active = models.BooleanField(default = True)
    def __str__(self):
        return self.email
    def getCompany(self):
        return self.company

class Query(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.user.first_name + " (" + str(self.date) + ")"
