# dashboard/urls.py
from django.urls import path, include
from system1.views import RegisterView, SendMessageView, ReceiveMessageView
from .views import dashboard_view
from django.contrib.auth.views import LoginView
from . import views 
from .views import custom_login
from .views import CustomLoginView


urlpatterns = [
    path('', dashboard_view, name='dashboard'),  # Dashboard view
    path('register/', RegisterView.as_view(), name='register'),  # Register view
    path('login/', CustomLoginView.as_view(), name='login'),
    path('accounts/login/', custom_login, name='login'),
    path('send/', SendMessageView.as_view(), name='send-message'),
    path('received/', ReceiveMessageView.as_view(), name='view-received-messages'),  # View received messages
    path('system1/', include('system1.urls')),  # Include system1 URLs
    path('system2/', include('system2.urls')),  # Include system2 URLs
    path('send_message/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
]
