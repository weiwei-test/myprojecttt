"""djangoProject URL Configuration

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
from django.contrib import admin
from django.urls import path

from myvue import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/login', views.login_demo),
    path('user/detail', views.detail_demo),
    path('user/logout', views.logout_demo),
    path('home/list', views.home_list),
    path('order/list', views.order),
    path('size/list', views.get_size),




]
