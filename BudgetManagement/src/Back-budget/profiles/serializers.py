from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth import get_user_model
from .models import Wallet


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'first_name', 'last_name', 'mobile', 'address']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
    

class UserProfileSerializer(serializers.ModelSerializer):
    wallet_balance = serializers.SerializerMethodField()
    monthly_budget = serializers.SerializerMethodField()  # New field

    class Meta:
        model = UserProfile
        fields = '__all__' 
        extra_fields = ['wallet_balance', 'monthly_budget']

    def get_wallet_balance(self, obj):
        try:
            return obj.wallet.balance
        except Wallet.DoesNotExist:
            return 0.00

    def get_monthly_budget(self, obj):  # New method
        try:
            return obj.wallet.monthly_budget
        except Wallet.DoesNotExist:
            return 0.00
    

    




