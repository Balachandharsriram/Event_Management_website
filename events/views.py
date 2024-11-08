from django.shortcuts import render, get_object_or_404
from .models import Event

def event_list(request):
    events = Event.objects.all()  # Get all events
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Get a specific event by ID
    return render(request, 'events/event_detail.html', {'event': event})
