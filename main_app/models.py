from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

# Create your models here.

class Lace(models.Model):
    style = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.style

    def get_absolute_url(self):
        return reverse('laces_detail', kwargs={'pk': self.id})

class Kick(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    releasedate = models.CharField(max_length=100)
    # Add a M:M relationship
    laces = models.ManyToManyField(Lace)
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('detail', kwargs={'kick_id': self.id})

    def viewed_for_today(self):
        return self.viewing_set.filter(date=date.today()).count() >= len(TIMES)

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