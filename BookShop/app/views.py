from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# Create your views here.
def home(req):
    return HttpResponse(render(req, 'home.html', {
        'books': Book.objects.all()
    }))


def book(req, slug):
    return HttpResponse(render(req, 'book.html', {
        'book': Book.objects.filter(slug=slug).get()
    }))
