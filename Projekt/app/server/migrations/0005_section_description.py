# Generated by Django 5.0 on 2024-01-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_remove_server_player_count_remove_server_rank_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
