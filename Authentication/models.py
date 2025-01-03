from email.policy import default
from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField(default=True)
    is_donor = models.BooleanField(default=False)
    is_fundRaiser = models.BooleanField(default=False)
    institution = models.CharField(max_length=200,default='')

class UserWallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
