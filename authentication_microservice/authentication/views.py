from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser, OTP
from .serializers import UserSerializer, OTPSerializer
from django.core.mail import send_mail
import random


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        otp_code = random.randint(100000, 999999)
        OTP.objects.create(user=user, otp_code=str(otp_code))
        send_mail(
            'Verify your email',
            f'Your OTP code is {otp_code}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def verify_otp(request):
    otp_code = request.data.get('otp_code')
    user_id = request.data.get('user_id')
    try:
        otp = OTP.objects.get(user_id=user_id, otp_code=otp_code, verified=False)
        otp.verified = True
        otp.save()
        return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
    except OTP.DoesNotExist:
        return Response({'message': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reset_password(request):
    email = request.data.get('email')
    try:
        user = CustomUser.objects.get(email=email)
        otp_code = random.randint(100000, 999999)
        OTP.objects.create(user=user, otp_code=str(otp_code))
        send_mail(
            'Reset your password',
            f'Your OTP code is {otp_code}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )
        return Response({'message': 'OTP sent to your email'}, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({'message': 'Email not found'}, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import User
# from .serializers import UserSerializer
#
# @api_view(['POST'])
# def register_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
