from django.db import models
from django.contrib.auth.models import User

class SentMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='system1_sent_messages')  # Unique related_name
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    message_type = models.CharField(max_length=50, choices=[('sent', 'Sent'), ('received', 'Received')], default='sent')

    class Meta:
        ordering = ['-timestamp']  # Order by latest first

    def __str__(self):
        return f"Message {self.message_type} by {self.user} at {self.timestamp}"

class ReceivedMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='system1_received_messages')  # Unique related_name
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']  # Order by latest first

    def __str__(self):
        return f"Received by {self.user} at {self.timestamp}"
