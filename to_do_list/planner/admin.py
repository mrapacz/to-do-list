from django.contrib import admin

# Register your models here.
from planner.models import Day, Event
admin.site.register(Day)
admin.site.register(Event)