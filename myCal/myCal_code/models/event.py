from django.db import models
from time import time
from datetime import datetime
class Event(models.Model):
    title= models.CharField(null=False, blank=False)
    description= models.TextField(null=False, blank=False)
    event_date= models.DateField(auto_now=False, auto_now_add=False)
    location = models.CharField(null=False, blank=False)
    start_time= models.CharField(null=False, blank=False)
    finish_time= models.CharField(null=False, blank=False)
    created_at= models.DateTimeField(null=False, auto_now_add=True)

    @classmethod
    def isTimeFormat(self):
        try:
            time.strptime(self.start_time, '%H:%M')
            time.strptime(self.finish_time, '%H:%M')
            return True
        except ValueError:
            return False
