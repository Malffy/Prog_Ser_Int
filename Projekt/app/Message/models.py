from django.db import models
from user.models import User

class Message(models.Model):
     sender = models.ForeignKey(User, related_name="sender")
     reciever = models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE)
     msg_content = models.TextField()
     created_at = models.DateTimeField()