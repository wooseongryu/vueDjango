"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mysite.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    # blog
    path('', HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls')),
    path('api/', include('api.urls')),

    path('api2/', include('api2.urls')),
]

# static함수를 사용해서 settings파일의 MEDIA_URL에 작성한 URL이 들어오면
# MEDIA_ROOT에서 파일을 찾아서 처리한다.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
