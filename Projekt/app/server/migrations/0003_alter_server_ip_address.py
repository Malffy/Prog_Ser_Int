# Generated by Django 5.0 on 2024-01-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_server_delete_serwer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]