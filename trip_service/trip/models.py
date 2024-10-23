from django.db import models

class Route(models.Model):
    route_id = models.CharField(max_length=10, primary_key=True, editable=False)
    user_id = models.CharField()
    route_name = models.CharField(max_length=100)
    route_origin = models.CharField(max_length=100)
    route_destination = models.CharField(max_length=100)
    route_stops = models.JSONField()

    def save(self, *args, **kwargs):
        if not self.route_id:
            # Get the count of existing Route objects and increment for the new ID
            last_id = Route.objects.count() + 1
            self.route_id = f"RT{str(last_id).zfill(8)}"  # RT00000001, RT00000002, etc.
        super(Route, self).save(*args, **kwargs)

    class Meta:
        ordering = ['route_name']  # Default ordering by route name
        unique_together = ['user_id', 'route_name']
        
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
            # Get the count of existing Trip objects and increment for the new ID
            last_id = Trip.objects.count() + 1
            self.trip_id = f"TP{str(last_id).zfill(8)}"  # TP00000001, TP00000002, etc.
        super(Trip, self).save(*args, **kwargs)

    def __str__(self):
        return self.trip_id
