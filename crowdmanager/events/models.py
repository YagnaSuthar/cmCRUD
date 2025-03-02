from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    eventname = models.CharField(max_length=100)
    event_description = models.TextField(blank=True,null=True,max_length=4000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-updated','-created']

    def __str__(self):
        return self.eventname

    