from rest_framework import serializers
from .models import SentMessage, ReceivedMessage
from .utils import decrypt_message

class SentMessageSerializer(serializers.ModelSerializer):
    decrypted_message = serializers.SerializerMethodField()

    class Meta:
        model = SentMessage
        fields = ['id', 'user', 'message', 'decrypted_message', 'timestamp', 'message_type']

    def get_decrypted_message(self, obj):
        try:
            return decrypt_message(obj.message)
        except Exception:
            return None  # Return None if decryption fails

class ReceivedMessageSerializer(serializers.ModelSerializer):
    decrypted_message = serializers.SerializerMethodField()

    class Meta:
        model = ReceivedMessage
        fields = ['id', 'user', 'message', 'decrypted_message', 'timestamp']

    def get_decrypted_message(self, obj):
        try:
            return decrypt_message(obj.message)
        except Exception:
            return None  # Return None if decryption fails
