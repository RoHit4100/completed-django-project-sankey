import os
import django
import random
from faker import Faker

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booking_service.settings')  # Replace with your project name
django.setup()

from booking.models import Booking  # Replace with your app model

fake = Faker()

def validate_trip_id(trip_id):
    # Validate the trip_id format
    return trip_id.startswith('TP') and trip_id[2:].isdigit() and len(trip_id) == 10

def generate_fake_booking_data(num_bookings=50):
    # Get the count of existing bookings to ensure unique ticket IDs
    existing_bookings_count = Booking.objects.count()

    for i in range(num_bookings):
        # Generate trip_id based on incremental nature
        trip_id = f'TP{str(i + 1).zfill(8)}'  # TP00000001, TP00000002, etc.
        
        if not validate_trip_id(trip_id):
            print(f"Invalid trip ID: {trip_id}")
            continue

        traveler_name = fake.name()
        traveler_number = f'{random.randint(6000000000, 9999999999)}'
        ticket_cost = round(random.uniform(50, 500), 2)
        traveler_email = fake.email()

        booking = Booking(
            trip_id=trip_id,
            traveler_name=traveler_name,
            traveler_number=traveler_number,
            ticket_cost=ticket_cost,
            traveler_email=traveler_email
        )
        booking.save()

if __name__ == '__main__':
    generate_fake_booking_data(50)  # Generate 50 fake bookings
    print("Successfully generated 50 fake bookings.")
