from django.db import models


# Create your models here.
class Account(models.Model):
    account_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
