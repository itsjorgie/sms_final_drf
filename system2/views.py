from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import ReceivedMessage, SentMessage
from .serializers import ReceivedMessageSerializer, SentMessageSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .utils import decrypt_message, encrypt_message
import requests, logging

# Sending messages
class SendMessageView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request):
        message = request.data.get("message")
        token = request.headers.get("Authorization")

        if token and token.startswith("Bearer "):
            token = token.split("Bearer ")[1]
        else:
            return Response({"error": "Authorization token is required"}, status=status.HTTP_401_UNAUTHORIZED)

        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Get the authenticated user
        user = request.user

        # Encrypt the message before saving and sending
        encrypted_message = encrypt_message(message)

        # Save the encrypted message to the database
        sent_message = SentMessage.objects.create(user=user, message=encrypted_message)

        # Update the URL to point to system2
        system2_url = 'http://127.0.0.1:8001/api/system1/received/'
        payload = {
            'message': encrypted_message  # Send the encrypted message
        }
        headers = {
            'Authorization': f'Bearer {token}'
        }

        try:
            response = requests.post(system2_url, json=payload, headers=headers)

            if response.status_code == 201:
                return Response({
                    "message": "Message sent and saved successfully",
                    "message_id": sent_message.id
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    "error": f"Failed to send message to System 1: {response.status_code} - {response.text}"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except requests.exceptions.RequestException as e:
            logging.error(f"Error sending message to System 2: {str(e)}")
            return Response({"error": "Failed to send message to System 1"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Receiving messages
class ReceiveMessageView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        encrypted_message = request.data.get("message")

        if not encrypted_message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Save the encrypted message directly
            received_message = ReceivedMessage.objects.create(
                user=request.user,
                message=encrypted_message  # Save as encrypted
            )

            # Optionally decrypt for verification or debugging
            decrypted_message = decrypt_message(encrypted_message)

            return Response({
                "message": "Message received and stored successfully",
                "message_id": received_message.id,
                "decrypted_message": decrypted_message  # For debugging (remove in production)
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error saving or decrypting message: {e}")
            return Response({"error": "Failed to save or decrypt message"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        # Fetch all received messages
        received_messages = ReceivedMessage.objects.all().order_by('-timestamp')
        decrypted_messages = []

        # Decrypt each message for display
        for msg in received_messages:
            try:
                decrypted_messages.append({
                    "id": msg.id,
                    "user": msg.user.username,
                    "message": decrypt_message(msg.message),  # Decrypt for display
                    "timestamp": msg.timestamp
                })
            except Exception as e:
                print(f"Error decrypting message ID {msg.id}: {e}")
                continue

        return Response(decrypted_messages, status=status.HTTP_200_OK)


# View sent messages
class ViewSentMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        messages = SentMessage.objects.filter(user=user)

        # Decrypt messages for display
        decrypted_messages = [
            {
                "id": msg.id,
                "message": decrypt_message(msg.message),
                "timestamp": msg.timestamp
            }
            for msg in messages
        ]

        return Response(decrypted_messages, status=status.HTTP_200_OK)

# User registration view
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username is already taken"}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

# User login view
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }, status=status.HTTP_200_OK)

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
