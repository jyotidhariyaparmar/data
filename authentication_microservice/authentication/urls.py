from django.urls import path
from .views import register_user, verify_otp, reset_password

urlpatterns = [
    path('register/', register_user),
    path('verify_otp/', verify_otp),
    path('reset_password/', reset_password),
]
















# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('register/', views.register_user, name='register'),
# ]
