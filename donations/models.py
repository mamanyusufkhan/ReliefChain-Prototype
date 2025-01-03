from datetime import date
from django.db import models
from Authentication.models import User
from events.models import Event
from django.utils import timezone

# Create your models here.
class Donation(models.Model):
    Donation_id = models.AutoField(primary_key=True)
    Event_Id = models.ForeignKey(Event, on_delete=models.CASCADE)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    DateTime = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"Donation #{self.Event_Id}"
