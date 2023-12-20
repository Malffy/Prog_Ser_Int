from django.db import models

class Serwer(models.Model):
    nazwa_serwera = models.CharField(max_length=255)
    adres_ip = models.GenericIPAddressField()
    liczba_graczy = models.IntegerField()
    mapa = models.CharField(max_length=255)
    pozycja_w_rankingu = models.IntegerField()
    liczba_glosow = models.IntegerField()

