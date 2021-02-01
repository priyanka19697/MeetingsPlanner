from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('rooms', views.meetingRooms, name='meetingRooms'),
    path('rooms/<int:id>', views.meetingRoom, name='meetingRoom'),
    path('new', views.new, name='meetingForm')

]
