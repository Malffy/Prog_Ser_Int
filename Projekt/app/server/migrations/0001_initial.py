# Generated by Django 5.0 on 2023-12-15 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serwer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_serwera', models.CharField(max_length=255)),
                ('adres_ip', models.GenericIPAddressField()),
                ('liczba_graczy', models.IntegerField()),
                ('mapa', models.CharField(max_length=255)),
                ('pozycja_w_rankingu', models.IntegerField()),
                ('liczba_glosow', models.IntegerField()),
            ],
        ),
    ]
