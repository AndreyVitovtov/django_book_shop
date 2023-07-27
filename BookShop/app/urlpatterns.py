from django.urls import path

from app.views import home, book

urlpatterns = [
    path('', home),
    path('book/<str:slug>', book),
]
