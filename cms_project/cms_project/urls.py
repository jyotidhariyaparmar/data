from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, PostViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]




# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, PostViewSet, LikeViewSet
#
# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'posts', PostViewSet)
# router.register(r'likes', LikeViewSet)
#
# urlpatterns = [
#     #     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
# ]
