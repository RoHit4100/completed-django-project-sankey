import os
import django
from faker import Faker
import random

# Set the Django environment settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trip_service.settings')  # Replace with your project name
django.setup()

from trip.models import Route, Trip  # Import your models

fake = Faker()

def create_dummy_routes(num=10):
    for _ in range(num):
        route_origin = fake.city()
        route_destination = fake.city()
        route_name = f'{route_origin} - {route_destination}'
        
        # Generate random route stops
        route_stops = [
            {
                'lat': round(random.uniform(50, 500), 2),
                'long': round(random.uniform(50, 500), 2),
                'stop_name': fake.city()
            }
            for _ in range(random.randint(1, 5))
        ]
        # Add origin and destination as the first and last stop
        route_stops.insert(0, {'lat': round(random.uniform(50, 500), 2), 'long': round(random.uniform(50, 500), 2), 'stop_name': route_origin})
        route_stops.append({'lat': round(random.uniform(50, 500), 2), 'long': round(random.uniform(50, 500), 2), 'stop_name': route_destination})
        
        # Create the Route instance
        route = Route(
            user_id=str(fake.random_int(min=1, max=100)),  # Generate random user_id as string
            route_name=route_name,
            route_origin=route_origin,
            route_destination=route_destination,
            route_stops=route_stops
        )
        route.save()  # Save to generate route_id
        print(f'Created route: {route.route_id} - {route.route_name}')

def create_dummy_trips(num=10):
    routes = Route.objects.all()  # Get all existing routes
    for _ in range(num):
        if not routes:
            print("No routes available to create trips.")
            return
        
        # Create the Trip instance
        trip = Trip(
            user_id=str(fake.random_int(min=1, max=1000)),  # Generate random user_id as string
            vehicle_id=fake.random_int(min=1, max=5000),  # Generate random vehicle ID
            route=random.choice(routes),  # Randomly assign an existing route
            driver_name=fake.name()
        )
        trip.save()  # Save to generate trip_id
        print(f'Created trip: {trip.trip_id} for route {trip.route.route_id}')

# Create dummy data
create_dummy_routes(50)  
create_dummy_trips(50)
