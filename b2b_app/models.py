from django.db import models

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
    contact_person = models.CharField(max_length = 250)
    contact_number = models.CharField(max_length = 12)
    search_sites = MultiSelectField(max_length = 100, choices = SITE_CHOICES)
    book_formats = MultiSelectField(max_length = 100, choices = BOOK_FORMATS)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 250)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    password = models.CharField(max_length = 150)
    active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.user.name + " (" + str(self.date) + ")"
