from django.db import models

class Booking(models.Model):
    ticket_id = models.CharField(max_length=10, primary_key=True, editable=False)  # Custom ID with prefix
    trip_id = models.CharField(max_length=10)
    traveler_name = models.CharField(max_length=100)
    traveler_number = models.CharField(max_length=10)
    ticket_cost = models.FloatField()
    traveler_email = models.EmailField()

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            # Get the count of existing Booking objects and increment for the new ID
            last_id = Booking.objects.count() + 1
            self.ticket_id = f"TK{str(last_id).zfill(8)}"  # TK00000001, TK00000002, etc.
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return self.ticket_id
