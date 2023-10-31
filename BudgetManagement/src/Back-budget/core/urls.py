from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    # ... other URL patterns
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]