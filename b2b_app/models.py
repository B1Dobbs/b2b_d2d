from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=250)
    contactEmail = models.EmailField(max_length = 250)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 250)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    queries = models.IntegerField(default = 0)

    def __str__(self):
        return self.name