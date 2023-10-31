from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.authtoken.models import Token
from core.models import User
from .serializers import UserRegistrationSerializer
from .models import Wallet
from .serializers import WalletSerializer


class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()  # Update the queryset to directly use User
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)


# Add more views as needed for creating, updating, or listing user profiles

# profile/views.py



class WalletListCreateView(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
