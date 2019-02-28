from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def about(request):
    return render(request, 'about.html')


def copyright(request):
    return render(request, 'copyright.html')


def creators(request):
    return render(request, 'creators.html')


def developers(request):
    return render(request, 'developers.html')


def history(request):
    return render(request, 'history.html')


def home(request):
    return render(request, 'home.html')


def movies(request):
    return render(request, 'movies.html')


def news(request):
    return render(request, 'news.html')


def privacy(request):
    return render(request, 'privacy.html')


def shows(request):
    return render(request, 'shows.html')


def single(request):
    return render(request, 'single.html')


def sports(request):
    return render(request, 'sports.html')


def terms(request):
    return render(request, 'terms.html')


def try_(request):
    return render(request, 'try.html')


def upload(request):
    return render(request, 'upload.html')


def press(request):
    return render(request, 'press.html')
