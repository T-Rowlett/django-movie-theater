from django.shortcuts import render
from app.models import Movie, Showing, Ticket

# Create your views here.


def home(request):
    movies = Movie.objects.all()
    return render(request, "base.html", {"movies": movies})


def new_ticket(request):
    if request == GET():
        return render(request, "new_ticket.html", )


def ticket_detail(request):
    pass
