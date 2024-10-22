import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from weather.models import WeatherData

API_KEY = 'c305c55e6597c04f5b60a16fcbe846df'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

class Command(BaseCommand):
    help = 'Fetch weather data from OpenWeatherMap API'

    def handle(self, *args, **kwargs):
        for city in CITIES:
            response = requests.get(URL.format(city=city, api_key=API_KEY)).json()
            weather_data = WeatherData(
                city=city,
                main=response['weather'][0]['main'],
                temp=kelvin_to_celsius(response['main']['temp']),
                feels_like=kelvin_to_celsius(response['main']['feels_like']),
                timestamp=datetime.fromtimestamp(response['dt']),
            )
            weather_data.save()
            self.stdout.write(f"Weather data for {city} saved.")
