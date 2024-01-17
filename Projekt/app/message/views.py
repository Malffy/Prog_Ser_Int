from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)