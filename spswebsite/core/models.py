from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    desc = models.TextField("Event description", blank=True, max_length=1500)
