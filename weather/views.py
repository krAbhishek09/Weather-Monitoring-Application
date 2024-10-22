from django.shortcuts import render
from django.db import models
from weather.models import WeatherData
from django.utils.timezone import now

# Define alert thresholds (you can make this user-configurable)
TEMP_THRESHOLD = 35.0  # Temperature alert threshold (Celsius)

def daily_summary(request):
    today = now().date()
    weather_today = WeatherData.objects.filter(timestamp__date=today)

    # Calculate daily aggregates
    avg_temp = weather_today.aggregate(models.Avg('temp'))['temp__avg']
    max_temp = weather_today.aggregate(models.Max('temp'))['temp__max']
    min_temp = weather_today.aggregate(models.Min('temp'))['temp__min']
    dominant_condition = (
        weather_today.values('main')
        .annotate(count=models.Count('main'))
        .order_by('-count')
        .first()
    )

    # Check if an alert condition is met (e.g., temp > 35°C)
    alert_message = None
    if max_temp and max_temp > TEMP_THRESHOLD:
        alert_message = f"⚠️ High Temperature Alert! Max temp: {max_temp}°C"

        # Log the alert to the console (can be extended to email alerts)
        print(alert_message)

    context = {
        'weather_today': weather_today,
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': dominant_condition,
        'alert_message': alert_message,
    }
    return render(request, 'weather/summary.html', context)
