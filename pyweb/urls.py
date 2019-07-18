# spring에서 메소드 위에 애노테이션 맾핑

from django.contrib import admin # -> import django.contrib.admin (어제했던 방식)
from django.urls import path # -> import django.urls.path (어제했던 방식)
from board import views

urlpatterns = [ # 맾핑 -> path('주소', '함수경로.함수이름')
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
]




"""pyweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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