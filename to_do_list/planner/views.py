from django.core.exceptions import ValidationError
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .models import Day, Event
from .forms import DayForm, EventForm


class IndexView(generic.ListView):
    template_name = 'planner/index.html'
    context_object_name = 'planned_days_list'

    def get_queryset(self):
        return Day.objects.all().order_by('date')


class DayView(generic.ListView):
    model = Event
    context_object_name = 'events_of_the_chosen_day_list'

    def get_context_data(self, **kwargs):
        context = super(DayView, self).get_context_data()
        context['day_date'] = self.kwargs['day_date']
        return context

    def get_queryset(self):
        return Day.objects.get(date=self.kwargs['day_date']).event_set.all().order_by('start_time')


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'planner/event_detail.html'
    context_object_name = 'current_event'


def day_new(request):
    if request.method == 'POST':
        form = DayForm(request.POST)
        if form.is_valid():
            entered_day = form.save()
            return redirect('/planner/' + str(entered_day.date))
    else:
        form = DayForm(initial={'date': 'yyyy-mm-dd'})
    return render(request, 'planner/day_new.html', {'form': form})


def event_new(request, **kwargs):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.day = Day.objects.get(date=kwargs['day_date'])
            new_event.save()
            return redirect('/planner/' + str(new_event.day.date) + "/" + str(new_event.id))
    else:
        form = EventForm()
    return render(request, 'planner/event_new.html', {'form': form, 'day_date': kwargs['day_date']})


def event_edit(request, id=None, **kwargs):
    if id:
        event = get_object_or_404(Event, pk=id)
    else:
        event = Event()

    form = EventForm(request.POST, instance=event, )
    if request.method == 'POST':
        try:
            if form.is_valid():
                new_event = form.save(commit=False)
                new_event.day = Day.objects.get(date=kwargs['day_date'])
                new_event.save()
                return redirect('/planner/' + str(new_event.day.date) + "/" + str(new_event.id))
        except TypeError:
            pass
    else:
        form = EventForm(instance=event)
    return render(request, 'planner/event_new.html', {'form': form, 'day_date': kwargs['day_date']})


def event_delete(request, **kwargs):
    event = get_object_or_404(Event, pk=kwargs['id'])
    if event:
        event.delete()
    return redirect('planner:day_view', day_date=kwargs['day_date'])


def day_delete(request, **kwargs):
    day = get_object_or_404(Day, date=kwargs['day_date'])
    if day:
        day.delete()
    return redirect('planner:index')
