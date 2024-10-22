from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    temp = models.FloatField()
    feels_like = models.FloatField()
    timestamp = models.DateTimeField()
