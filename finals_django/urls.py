"""finals_django URL Configuration

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
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/system1/', include('system1.urls')),  # Service1 URL routing
    path('api/system2/', include('system2.urls')),  # Service2 URL routing
    path('dashboard/', include('dashboard.urls')),   # Dashboard URL routing

    path('', include('system1.urls')),
    path('', include('system2.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Built-in login view
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Built-in logout view

]

