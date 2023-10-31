from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'mobile', 'address')  # Customize this based on your requirements
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], mobile=validated_data['mobile'], address=validated_data['address'])
        user.set_password(validated_data['password'])
        user.save()
        return user
