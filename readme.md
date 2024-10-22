Weather Monitoring Application
A real-time weather monitoring system that retrieves data from the OpenWeatherMap API, displays summaries, and triggers alerts based on user-defined thresholds. The system is built using Django and runs inside Docker containers with PostgreSQL as the database.

Features
Real-time Weather Data for cities: Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad
Daily Summary: Displays average, maximum, and minimum temperatures along with the dominant weather condition
Alerts: Triggered when temperatures exceed configurable thresholds
UI Dashboard: Displays weather summaries and updates with responsive design and animations
Docker Support: Containerized with Docker and Docker Compose
Prerequisites
Docker: Install Docker
Docker Compose: Install Docker Compose
OpenWeatherMap API Key: Get API Key
Installation Steps
1. Clone the Repository
bash
Copy code
git clone https://github.com/krAbhishek09/weather-monitoring-app.git
cd weather-monitoring-app
2. Set Up Environment Variables
Create a .env file in the project root and add:

makefile
Copy code
OPENWEATHER_API_KEY=your_openweather_api_key_here
ALERT_THRESHOLD_TEMP=35  # Threshold for alerts (in °C)
3. Build the Docker Containers
bash
Copy code
docker-compose build
4. Run the Containers
bash
Copy code
docker-compose up
5. Apply Database Migrations
Open a new terminal and run:

bash
Copy code
docker-compose exec web python manage.py migrate
6. Create a Superuser (Optional)
bash
Copy code
docker-compose exec web python manage.py createsuperuser
Usage
Access the Web Interface:
Open your browser and visit:
http://localhost:8000

View Weather Summary:
The dashboard displays daily weather summaries and hourly updates.

Alerts:
If the temperature exceeds the threshold, alerts are shown on the UI.

Stop the Containers:
Press Ctrl + C or run:

bash
Copy code
docker-compose down
Configuration Options
Cities: Modify the list of cities in the Django views.
Thresholds: Adjust the alert temperature in the .env file.
Weather Parameters: Extend the application to display additional parameters like humidity or wind speed.
Project Structure
bash
Copy code
weather-monitoring-app/
│
├── Dockerfile              # Docker build instructions  
├── docker-compose.yml      # Docker Compose configuration  
├── requirements.txt        # Dependencies  
├── .env                    # Environment variables  
├── manage.py               # Django management script  
├── app/                    # Django app directory  
│   ├── models.py           # Database models  
│   ├── views.py            # Application views  
│   ├── templates/          # HTML templates  
│   ├── migrations/         # Database migrations  
│   └── ...  
└── README.md               # Documentation  
Technologies Used
Python 3.9
Django 4.2.6
PostgreSQL
Docker & Docker Compose
OpenWeatherMap API
Test Cases
System Setup:
Verify that containers start successfully and connect to the API.

Data Retrieval:
Ensure API calls retrieve weather data and process it correctly.

Temperature Conversion:
Check Kelvin to Celsius conversion based on user settings.

Alerts:
Test alert triggers when temperature exceeds the threshold.

Troubleshooting
Database Issues:
Ensure PostgreSQL container is running and the credentials match the configuration.

API Key Errors:
Check if the OpenWeatherMap API key in the .env file is valid.

Port Conflicts:
If port 8000 is in use, change it in the docker-compose.yml:

yaml
Copy code
ports:
  - "8080:8000"
Contributing
Feel free to open issues or submit pull requests with suggestions or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
OpenWeatherMap for the API
Django for the framework
Docker for containerization
