from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    subject = models.CharField(max_length=255)   # <- this must exist
    body = models.TextField()                     # <- this must exist
    sent_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"
    

    