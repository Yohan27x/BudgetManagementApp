# urls.py

from django.urls import path
from backend.views import SpendingCategoryListCreateView, ExpenseListCreateView, BudgetListCreateView

urlpatterns = [
    path('spending_categories/', SpendingCategoryListCreateView.as_view(), name='spending-category-list-create'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('budgets/', BudgetListCreateView.as_view(), name='budget-list-create'),
    # ... other patterns
]
