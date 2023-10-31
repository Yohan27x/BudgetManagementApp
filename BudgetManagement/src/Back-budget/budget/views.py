from rest_framework import generics
from .models import Budget, SpendingCategory, Expense
from .serializers import BudgetSerializer, SpendingCategorySerializer, ExpenseSerializer

class SpendingCategoryListCreateView(generics.ListCreateAPIView):
    queryset = SpendingCategory.objects.all()
    serializer_class = SpendingCategorySerializer

class SpendingCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpendingCategory.objects.all()
    serializer_class = SpendingCategorySerializer

class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class BudgetListCreateView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
