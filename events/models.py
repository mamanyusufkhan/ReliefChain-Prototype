from datetime import datetime
from django.utils import timezone
from django.db import models
from Authentication.models import User


# Create your models here.
class Event(models.Model):
    Event_ID = models.AutoField(primary_key=True)
    Event_name = models.CharField(max_length=255)
    Event_details = models.TextField()
    FundRaiser = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.CharField(max_length=255)
    Division = models.CharField(max_length=255)
    District = models.CharField(max_length=255)
    Amount_to_be_raised = models.DecimalField(max_digits=10, decimal_places=2)
    Minimum_amount_to_be_raised = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Starts_at = models.DateTimeField(default=timezone.now)
    Ends_at = models.DateTimeField(default=timezone.now)
    Is_approved = models.BooleanField(default=False)
    Event_status = models.CharField(max_length=10, choices=[('live', 'Live'), ('past', 'Past')])

    def __str__(self):
        return self.Event_name


class Escrow_Account(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)