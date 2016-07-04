from django.test import TestCase

from planner.forms import EventForm, DayForm


class MyTests(TestCase):
    def test_day_form(self):
        form_data = {'date': '2015-02-03'}
        form = DayForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {'date': '2015-02-03s'}
        form = DayForm(data=form_data)
        self.assertTrue(not form.is_valid())

    def test_event_form(self):
        form_data = {'title': 'some title', 'start_time': '02:12:12', 'end_time': '03:12:14',
                     'description': 'some description'}
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid())

        # end time > start time
        form_data['start_time'] = '13:13:00'
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())
