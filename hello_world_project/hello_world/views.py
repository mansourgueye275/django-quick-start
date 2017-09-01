from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index(request):
    return HttpResponse('<html><body><h1>hello world!<h1></body></html>')


def about(request):
    return HttpResponse(
        "Here  is the about Page. Want to return home? <a href='/'>Black Home</a>"
    )


def better(request):
    t = loader.get_template('betterhello.html')
    c = Context({'current_time': datetime.now(), })
    return HttpResponse(t.render(c))
