from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import Event
from .forms import EventForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def eventsHome(request):
    events = Event.objects.all()
    context= {
        'events':events,
    }
    return render(request,'events/event_main.html',context)

def event(request,pk):
    event = Event.objects.get(id=pk)

    context = {
        'event':event,
    } 
    return render(request,'events/event.html',context)

@login_required(login_url='login')
def createForm(request):
   form = EventForm()
   if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            
            event = form.save()
            event = form.save(commit=False)
            event.host = request.user
            event.save()
            return redirect('eventsHome')
   context = {
       'form':form,
    }
   return render(request,'events/event_form.html',context)

@login_required(login_url='login')
def eventDelete(request,pk):
    event = Event.objects.get(id=pk)
    # event = get_object_or_404(Event, id=pk)

    # if request.user!= event.host:
    #     return HttpResponse('You are not allowed here!!')
        
    if request.method == "POST":
        event.delete()
        return redirect('eventsHome')
    
    return render(request,'events/event_delete.html',{'obj':event})

@login_required(login_url='login')
def updateEvent(request,pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    if request.user != event.host:
        return HttpResponse('You can not have access to edit event')
    
    if request.method == "POST":
        form = EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect('eventsHome')
        
    context = {
        'form':form,
    }
    return render(request,'events/event_form.html',context)