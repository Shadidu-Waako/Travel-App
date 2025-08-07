from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Trip table -> city, country, start_date, end_date, owner
class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=3)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')

    def __str__(self):
        return f"{self.city}-{self.country}"