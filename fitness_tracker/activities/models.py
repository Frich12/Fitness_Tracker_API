from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Weightlifting', 'Weightlifting'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(choices=ACTIVITY_TYPES, max_length=20)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")  
    distance = models.FloatField(null=True, blank=True, help_text="Distance in Kilometers")  
    calories_burned = models.FloatField(null=True, blank=True, help_text="Calories burned")
    date = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.activity_type} on {self.date}'


