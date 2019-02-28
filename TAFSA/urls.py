"""TAFSA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatte rns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload, name='upload'),
    path('try/', views.try_, name='try'),
    path('terms/', views.terms, name='terms'),
    path('sports/', views.sports, name='sports'),
    path('single/', views.single, name='single'),
    path('shows/', views.shows, name='shows'),
    path('privacy/', views.privacy, name='privacy'),
    path('press/', views.press, name='press'),
    path('news/', views.news, name='news'),
    path('movies/', views.movies, name='movies'),
    path('', views.home, name='index'),
    path('history/', views.history, name='history'),
    path('developers/', views.developers, name='developers'),
    path('creators/', views.creators, name='creators'),
    path('copyright/', views.copyright, name='copyright'),
    path('about/', views.about, name='about'),
    path(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
