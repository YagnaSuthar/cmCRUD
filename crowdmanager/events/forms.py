from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["eventname", "event_description"]
        