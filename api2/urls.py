# from django.urls import path, include
# from rest_framework import routers
#
# from api2.views import UserViewSet, PostViewSet, CommentViewSet
#
# # 디폴트 라우터를 사용해서
# router = routers.DefaultRouter()
# # 'users'라는 url에 UserViewSet을 맵핑한다
# router.register(r'user', UserViewSet)
# router.register(r'post', PostViewSet)
# router.register(r'comment', CommentViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path

from api2 import views

urlpatterns = [
    path('post/', views.PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post-detail'),
    path('comment/', views.CommentCreateAPIView.as_view(), name='comment-list'),
]
