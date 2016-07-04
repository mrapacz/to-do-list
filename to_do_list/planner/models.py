from datetime import time
from django.db import models


class Day(models.Model):
    date = models.DateField('day\'s happening time', unique=True)

    def __str__(self):
        return self.date.strftime("%A %d. %B %Y")


class Event(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    title = models.CharField(default="empty event title", max_length=64)
    description = models.TextField(default="empty description.")
    start_time = models.TimeField(default=time.min)
    end_time = models.TimeField(default=time.max)

    def __str__(self):
        return str(self.title) + " (" + str(self.start_time) + " - " + str(self.end_time) + ")"
