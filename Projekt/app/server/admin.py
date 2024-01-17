from django.contrib import admin

from .models import Server, Stats, Vote, Section, Post

# Register your models here.
admin.site.register(Server)
admin.site.register(Stats)
admin.site.register(Vote)
admin.site.register(Section)
admin.site.register(Post)
