from django.urls import path
from .views import SendMessageView, RegisterView, ViewSentMessagesView, ReceiveMessageView
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('send/', SendMessageView.as_view(), name='send-message'),
    path('sent-messages/', ViewSentMessagesView.as_view(), name='view-sent-messages'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('received/', ReceiveMessageView.as_view(), name='view-received-messages'),
]
