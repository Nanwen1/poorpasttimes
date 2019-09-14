from django.urls import path
from django.urls import include, path
from . import views


app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # event-finder/my-account
    path('newEventForm/', views.NewEventView.as_view(), name= 'NewEventForm'),
    # event-finder/form
    path('my-account/', views.account, name='account'),
]