from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting

# Create your views here.


def welcome(request):
    # return HttpResponse("Welcome to the meeting planner")
    return render(request, 'website/welcome.html', {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def aboutMe(request):
    return HttpResponse(" I am priyanka. I have been working as a software developer for the past 2.5 years" +
                        "and as a marketer  since the past 3 months")
