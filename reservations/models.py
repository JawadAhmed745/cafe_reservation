from django.db import models

# Create your models here.
from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    guest_count = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=10,
        choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')],
        default='confirmed'
    )

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
