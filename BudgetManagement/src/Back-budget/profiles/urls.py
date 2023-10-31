from django.urls import path
from profiles.views import UserProfileDetailView

urlpatterns = [
    # Add URL patterns for user profiles here
    path('profiles/<int:pk>/', UserProfileDetailView.as_view(), name='user-profile-detail'),
    # Add more URL patterns as needed
]
