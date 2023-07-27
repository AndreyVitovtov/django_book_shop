from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from comments.forms import CommentForm


# Create your views here.
def home(req):
    return HttpResponse(render(req, 'app/home.html', {
        'books': Book.objects.all()
    }))


def book(req, slug):
    book = Book.objects.get(slug=slug)
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
        return redirect(req.path)
    else:
        form = CommentForm(initial={'book': book})

    comments = book.comments.all()
    return HttpResponse(render(req, 'app/book.html', {
        'book': book,
        'comments': comments,
        'comments_count': comments.count(),
        'form': form
    }))
