from django import forms
from django.core.exceptions import ValidationError

from .models import Day, Event


class DayForm(forms.ModelForm):
    error_css_class = 'alert alert-danger'

    class Meta:
        model = Day
        fields = ('date',)

    def __init__(self, *args, **kwargs):
        super(DayForm, self).__init__(*args, **kwargs)
        self.fields['date'].label = 'Select a date:'


class EventForm(forms.ModelForm):
    #errorlist_css_class = 'alert alert-danger'

    class Meta:
        model = Event
        fields = ('title', 'start_time', 'end_time', 'description',)

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time > end_time:
            raise ValidationError('Start time cannot be later than end time.')
        return cleaned_data
