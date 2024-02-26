from rest_framework import serializers
from .models import CustomUser, OTP

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'phone_number', 'last_name']

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['otp_code', 'verified']


# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'email', 'phone_number', 'password']
#         extra_kwargs = {'password': {'write_only': True}}














# from rest_framework import serializers
# from .models import User
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # fields='__all__'
#         fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'is_verified']
