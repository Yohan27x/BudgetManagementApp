# budget/models.py
from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings
from django.conf import settings
from profiles.models import UserProfile


class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0.01)]  # Ensure the budget amount is positive
    )
    start_date = models.DateField()
    end_date = models.DateField()

    # Add any other relevant fields as needed

    def __str__(self):
        return f"{self.user.email}'s Budget"


class SpendingCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    # Add any other relevant fields as needed

    def __str__(self):
        return self.name
    



class Expense(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='expenses')  # Adding ForeignKey to UserProfile
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    category = models.ForeignKey('budget.SpendingCategory', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} - {self.category.name}"
    
    def save(self, *args, **kwargs):
        # If this expense is being created for the first time
        if not self.pk:
            # Deduct the expense amount from the user's wallet
            wallet = self.user.wallet
            wallet.balance -= self.amount
            wallet.save()
        super(Expense, self).save(*args, **kwargs)
