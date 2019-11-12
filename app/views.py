from django.shortcuts import render, redirect
from app.models import Movie, Showing, Ticket

# Create your views here.


def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})


def new_ticket(request, id):
    tickets = Ticket.objects.get(id=id)
    if request == "GET":
        return render(request, "new_ticket.html", {"tickets": tickets})
    if request.method == "POST":
        return redirect("ticket_detail", movie.id)


def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, "ticket_detail.html", {"ticket": ticket})