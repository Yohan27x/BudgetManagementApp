# budget/models.py
from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings
from django.conf import settings

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
    


class SpendingCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    category = models.ForeignKey('budget.SpendingCategory', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} - {self.category.name}"