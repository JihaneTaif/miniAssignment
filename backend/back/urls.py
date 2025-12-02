"""
URL configuration for back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# API URL Configuration
api_patterns = [
    # Authentication
    path('', include('users.urls')),
    
    # App endpoints
    path('', include('leads.urls')),
    path('', include('clients.urls')),
    path('', include('products.urls')),
    path('', include('claims.urls')),
]

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    
    # API v1
    path('api/v1/', include(api_patterns)),
    
    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # Health check endpoint
    path('health/', lambda request: JsonResponse({'status': 'healthy'})),
]
