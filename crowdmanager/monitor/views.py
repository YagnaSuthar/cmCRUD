from django.shortcuts import render,get_object_or_404
from events.models import Event
# Create your views here.

def monitorHome(request,pk):
    event = get_object_or_404(Event,id=pk)
    context = {
        'event':event,
    }

    return render(request,'monitor/monitor_home.html',context)
