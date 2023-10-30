from django.urls import path
from backend.views import SpendingCategoryListCreateView, SpendingCategoryDetailView, ExpenseListCreateView, ExpenseDetailView, BudgetListCreateView, BudgetDetailView

urlpatterns = [
    path('spending_categories/', SpendingCategoryListCreateView.as_view(), name='spending-category-list-create'),
    path('spending_categories/<int:pk>/', SpendingCategoryDetailView.as_view(), name='spending-category-detail'),
    
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),

    
    path('budgets/', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),
    
    # ... other patterns
]
