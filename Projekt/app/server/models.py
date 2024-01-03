from django.db import models
from app import settings


class Server(models.Model):
    server_name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(null=True)
    map = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.server_name}'


class Stats(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    player_count = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return f'{self.server}'


class Vote(models.Model):
    VOTE = {
        "YES": "YES",
        "NO": "NO"
    }
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    user_who_voted = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vote = models.CharField(max_length=255, choices=VOTE)

    def __str__(self):
        return f'{self.user_who_voted} - {self.vote} '


class Section(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    server_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.server} - {self.server_owner} '


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.section} - {self.user} - {self.title}'
