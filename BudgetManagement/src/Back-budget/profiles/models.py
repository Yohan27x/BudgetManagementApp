from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    budget = models.OneToOneField('budget.Budget', on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return self.user.email
    

class Wallet(models.Model):
    user = models.OneToOneField('profiles.UserProfile', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # The fixed budget

    def __str__(self):
        return f"{self.user}'s wallet - {self.balance}"
