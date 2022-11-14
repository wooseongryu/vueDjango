from django.urls import path, include
from rest_framework import routers

from api2.views import UserViewSet, PostViewSet

# 디폴트 라우터를 사용해서
router = routers.DefaultRouter()
# 'users'라는 url에 UserViewSet을 맵핑한다
router.register(r'user', UserViewSet)
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

