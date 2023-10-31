"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# urls.py

from django.urls import path
from budget.views import SpendingCategoryListCreateView, ExpenseListCreateView, BudgetListCreateView,SpendingCategoryDetailView,ExpenseDetailView,BudgetDetailView
from profiles.views import UserRegistrationView, WalletListCreateView, WalletRetrieveUpdateDestroyView
from .views import home



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home-json'),  # Empty path directs to the home view
    path('spending_categories/', SpendingCategoryListCreateView.as_view(), name='spending-category-list-create'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('budgets/', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('spending_categories/<int:pk>/', SpendingCategoryDetailView.as_view(), name='spending-category-detail'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),
    path('wallets/', WalletListCreateView.as_view(), name='wallet-list-create'),
    path('wallets/<int:pk>/', WalletRetrieveUpdateDestroyView.as_view(), name='wallet-retrieve-update-delete')


    
]


