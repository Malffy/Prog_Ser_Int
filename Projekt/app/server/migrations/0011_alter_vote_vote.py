# Generated by Django 5.0 on 2024-01-17 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_rename_rank_stats_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=255),
        ),
    ]