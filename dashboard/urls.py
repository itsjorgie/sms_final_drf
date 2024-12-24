from django.urls import path, include
from system1.views import RegisterView, LoginView, SendMessageView, ReceiveMessageView
from .views import dashboard_view, user_home
from . import views


urlpatterns = [
    path('', dashboard_view, name='dashboard'),  # Dashboard view
    path('userhome/', user_home, name='user_home'),
    path('register/', RegisterView.as_view(), name='register'),  # Register view
    path('login/', LoginView.as_view(), name='login'),  # Login view
    path('userhome/', views.user_home, name='userhome'),
    path('send/', SendMessageView.as_view(), name='send-message'),  # Send message view
    path('received/', ReceiveMessageView.as_view(), name='view-received-messages'),  # View received messages
    path('system1/', include('system1.urls')),  # Include system1 URLs
    path('system2/', include('system2.urls')),  # Include system2 URLs
]
