from django.db import models

from user.models import User


class Server(models.Model):
    server_name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(null=True)
    map = models.CharField(max_length=255)

class Stats(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    player_count = models.IntegerField()
    rank = models.IntegerField()

class Vote(models.Model):
    VOTE = {
        "YES": "YES",
        "NO": "NO"
    }
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    user_who_voted = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.CharField(max_length=255, choices=VOTE)

class Section(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    server_owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()





