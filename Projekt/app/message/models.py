from django.db import models
from user.models import User

class Message(models.Model):
     sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
     reciever = models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE)
     subject = models.CharField(max_length=255)
     msg_content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return f'{self.sender} -> {self.reciever}: {self.subject}'