"""olya_nail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
import os

from .yasg import urlpatterns as doc_urls
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path(f'{str(os.getenv("ADMIN_ADDRESS"))}/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/users/', include('users.urls')),
    path('api/v1/instagram/', include('instagram.urls')),
    path('api/v1/questions/', include('questions.urls')),
    path('api/v1/services/', include('services.urls')),
    path('api/v1/dates/', include('available_dates.urls')),
    path('api/v1/orders/', include('orders.urls')),
    path('api/v1/admin/', include('admin_panel.urls')),

]

urlpatterns += doc_urls

admin.site.site_title = "Olya Nail"
admin.site.site_header = "Маникюр Минск"
