# Generated by Django 5.0 on 2024-01-17 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_delete_onlineuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote',
            field=models.BooleanField(),
        ),
    ]
