from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, generics, permissions, status

from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Server, Stats, Vote, Section, Post
from .serializers import ServerSerializer, StatsSerializer, VoteSerializer, SectionSerializer, PostSerializer



# Create your views here.


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Dostęp tylko do właściciela obiektu, edycja tylko przez właściciela.
    """

    def has_object_permission(self, request, view, obj):
        # Dozwól zawsze GET, HEAD, lub OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # Dozwól edycję lub usunięcie tylko właścicielowi obiektu
        return obj.user == request.user

class ServerViewSet(viewsets.ModelViewSet):
    serializer_class = ServerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly, )
    queryset = Server.objects.all()


class StatsViewSet(viewsets.ModelViewSet):
    serializer_class = StatsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly, )
    queryset = Stats.objects.all()


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Vote.objects.all()

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        server = get_object_or_404(Server, id=pk)
        user = request.user

        # Sprawdź, czy użytkownik już zagłosował
        existing_vote = Vote.objects.filter(server=server, user_who_voted=user).first()
        if existing_vote:
            return Response({'detail': 'You have already voted for this server.'}, status=status.HTTP_400_BAD_REQUEST)

        # Zapisz nowy głos
        vote = request.data.get('vote', None)
        if vote not in ['YES', 'NO']:
            return Response({'detail': 'Invalid vote value.'}, status=status.HTTP_400_BAD_REQUEST)

        Vote.objects.create(server=server, user_who_voted=user, vote=vote)

        # Aktualizuj statystyki
        stats, created = Stats.objects.get_or_create(server=server)
        if vote == 'YES':
            stats.votes += 1
        else:
            stats.votes -= 1
        stats.save()

        return Response({'detail': 'Vote submitted successfully.'}, status=status.HTTP_201_CREATED)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        # Zwróć wpisy tylko dla zalogowanego użytkownika
        return Post.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Przypisz zalogowanego użytkownika jako autora wpisu
        serializer.save(user=self.request.user)

class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly, )
    queryset = Section.objects.all()
