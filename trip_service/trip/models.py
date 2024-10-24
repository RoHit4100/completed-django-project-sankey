from django.db import models
import time
import random

class Route(models.Model):
    route_id = models.CharField(max_length=10, primary_key=True, editable=False)
    user_id = models.CharField()
    route_name = models.CharField(max_length=100)
    route_origin = models.CharField(max_length=100)
    route_destination = models.CharField(max_length=100)
    route_stops = models.JSONField()

    def save(self, *args, **kwargs):
        if not self.route_id:
            epoch_time = str(int(time.time()))
            random_num = random.randint(10, 99) # this will give the random number from 0-99
            # print(epoch_time)
            # Use the last 6 digits of the epoch time
            epoch_part = epoch_time[-6:]
            unique_key = f'TK{epoch_part}{random_num}'
            # check if this unique key exists in the table or not
            while Route.objects.filter(route_id=unique_key).exists():
                epoch_time = str(int(time.time()))
                random_num = random.randint(0, 99) # this will give the random number from 0-99
                # print(epoch_time)
                # Use the last 6 digits of the epoch time
                epoch_part = epoch_time[-6:]
                unique_key = f'RT{epoch_part}{random_num}'
                
            self.route_id = unique_key
        super(Route, self).save(*args, **kwargs)


    class Meta:
        ordering = ['route_name']  # Default ordering by route name
        # unique_together = ['user_id', 'route_name']
        
    def __str__(self):
        return self.route_name


class Trip(models.Model):
    trip_id = models.CharField(max_length=10, primary_key=True, editable=False)
    user_id = models.CharField()
    vehicle_id = models.IntegerField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.trip_id:
            epoch_time = str(int(time.time()))
            random_num = random.randint(10, 99) # this will give the random number from 0-99
            # print(epoch_time)
            # Use the last 6 digits of the epoch time
            epoch_part = epoch_time[-6:]
            unique_key = f'TK{epoch_part}{random_num}'
            # check if this unique key exists in the table or not
            while Trip.objects.filter(trip_id=unique_key).exists():
                epoch_time = str(int(time.time()))
                random_num = random.randint(0, 99) # this will give the random number from 0-99
                # print(epoch_time)
                # Use the last 6 digits of the epoch time
                epoch_part = epoch_time[-6:]
                unique_key = f'TP{epoch_part}{random_num}'
                
            self.trip_id = unique_key
        super(Trip, self).save(*args, **kwargs)

    def __str__(self):
        return self.trip_id
