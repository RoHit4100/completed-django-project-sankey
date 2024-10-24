from django.db import models
import time
import random
class Booking(models.Model):
    ticket_id = models.CharField(max_length=10, primary_key=True, editable=False)  # Custom ID with prefix
    trip_id = models.CharField(max_length=10)
    traveler_name = models.CharField(max_length=100)
    traveler_number = models.CharField(max_length=10)
    ticket_cost = models.FloatField()
    traveler_email = models.EmailField()

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            # get the count of existing Booking objects and increment for the new ID
            # last_id = Booking.objects.count() + 1
            # self.ticket_id = f"TK{str(last_id).zfill(8)}"  # TK00000001
            epoch_time = str(int(time.time()))
            random_num = random.randint(10, 99) # this will give the random number from 0-99
            # print(epoch_time)
            # Use the last 6 digits of the epoch time
            epoch_part = epoch_time[-6:]
            unique_key = f'TK{epoch_part}{random_num}'
            # check if this unique key exists in the table or not
            while Booking.objects.filter(ticket_id=unique_key).exists():
                epoch_time = str(int(time.time()))
                random_num = random.randint(0, 99) # this will give the random number from 0-99
                # print(epoch_time)
                # Use the last 6 digits of the epoch time
                epoch_part = epoch_time[-6:]
                unique_key = f'TK{epoch_part}{random_num}'
                
            self.ticket_id = unique_key
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return self.ticket_id
