from django.shortcuts import render, HttpResponse, redirect
from .models import *

infaAU = InfaAboutUs.objects.all()
imagesOW = ImagesOurWorks.objects.all()

game_info = [{"game" : {"name":"Fruit Fight","link": "#"}}]
ourGamesContext =  {"name_of_page": "OUR GAMES","games" : game_info}
aboutUsContext = {'name_of_page': "ABOUT US", 'paragraphs': infaAU}

# Create your views here.
def AboutUs(request):
    return render(request,'Main_page/AboutUs.html',context=aboutUsContext)

def OurWorks(request):
    return render(request,'Main_page/OurWorks.html',{'name_of_page': "OUR WORKS", 'imagesOfWorks': imagesOW})

def OurGames(request):
        return redirect('/GIDACLUB/AboutUs/')

def Statistics(request):
    return render(request,'Main_page/Statistics.html',{'name_of_page': "STATISTICS"})

def Documentation(request):
    return render(request,'Main_page/Documentation.html',{'name_of_page': "DOCUMENTATION"})

def TelegramBot(request):
    return render(request,'Main_page/TelegramBot.html',{'name_of_page': "TELEGRAM BOT"})
