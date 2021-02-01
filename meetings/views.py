from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Meeting, MeetingRoom

# Create your views here.


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def meetingRooms(request):
    return render(request, "meetings/meetingRooms.html", {"meetingRooms":  MeetingRoom.objects.all()})


def meetingRoom(request, id):
    meetingRoom = get_object_or_404(MeetingRoom, pk=id)
    return render(request, "meetings/meetingRoom.html", {"meetingRoom": meetingRoom})


MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == "POST":
        # rorm has been submitted
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
