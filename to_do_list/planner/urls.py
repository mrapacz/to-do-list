from django.conf.urls import url

from . import views

app_name = 'planner'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<day_date>[0-9]{4}-[0-9]{2}-[0-9]{2})$', views.DayView.as_view(), name='day_view'),
    url(r'^(?P<day_date>[0-9]{4}-[0-9]{2}-[0-9]{2})/(?P<pk>[0-9]+)/$', views.EventDetailView.as_view(),
        name='event_details'),
    url(r'day_new/$', views.day_new, name='day_new'),
    url(r'^(?P<day_date>[0-9]{4}-[0-9]{2}-[0-9]{2})/event_new/$', views.event_new, name='event_new'),
    url(r'^(?P<day_date>[0-9]{4}-[0-9]{2}-[0-9]{2})/event_edit#id=(?P<id>[0-9]+)/$', views.event_edit,
        name='event_edit'),
    url(r'^(?P<day_date>[0-9]{4}-[0-9]{2}-[0-9]{2})/event_delete#id=(?P<id>[0-9]+)/$', views.event_delete,
        name='event_delete'),
    url(r'^(?P<day_date>[0-9]{4}-[0-9]{2}-[0-9]{2})/day_delete/$', views.day_delete,
        name='day_delete'),
]
