
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('AboutUs/', views.AboutUs, name='about_us'),
    path('OurWorks/', views.OurWorks, name='our_works'),
    path('OurGames/', views.OurGames, name='our_games'),
    path('Statistics/', views.Statistics, name='statistics'),
    path('Documentation/', views.Documentation, name='documentation'),
    path('TelegramBot/', views.TelegramBot, name='telegram_bot')
]
