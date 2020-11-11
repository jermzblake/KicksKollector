from django.db import models
from django.urls import reverse

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

# Create your models here.
class Kick(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    releasedate = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('detail', kwargs={'kick_id': self.id})

class Viewing(models.Model):
    date = models.DateField('viewing date')
    timeslot = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )
    #create a kick_id FK
    kick = models.ForeignKey(Kick, on_delete=models.CASCADE)

    def __str__(self):
        return(f'{self.get_timeslot_display()} on {self.date}')

      # change the default sort
    class Meta:
        ordering = ['-date']