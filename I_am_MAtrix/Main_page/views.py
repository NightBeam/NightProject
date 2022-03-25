from django.shortcuts import render, HttpResponse, redirect
from .models import *

infaAU = InfaAboutUs.objects.all()
videoOW = VideoOurWorks.objects.all()
datasDOC = ProgramsInfa.objects.all()
datasWeAre = We.objects.all()
datasTypeOfModeling = TypeOfModeling.objects.all()
datasTOM = list()
for i in datasTypeOfModeling:
    datasTOM.append(str(i.number))

game_info = [{"game" : {"name":"Fruit Fight","link": "#"}}]
ourGamesContext =  {"name_of_page": "OUR GAMES","games" : game_info}
aboutUsContext = {'name_of_page': "ABOUT US", 'paragraphs': infaAU,'weAre':datasWeAre}
ourWorksContext = {"name_of_page": "OUR WORKS",'videoOfWorks': videoOW}
documentationContext = {'name_of_page':"DOCUMENTATION", 'programs':datasDOC}
statisticsContext = {'name_of_page':"STATISTICS",'typeOfModeling':datasTOM}
# Create your views here.
def AboutUs(request):
    return render(request,'Main_page/AboutUs.html',context=aboutUsContext)

def OurWorks(request):
    return render(request,'Main_page/OurWorks.html',context=ourWorksContext)

def OurGames(request):
        return redirect('/GIDACLUB/AboutUs/')

def Statistics(request):
    return render(request,'Main_page/Statistics.html',context=statisticsContext)

def Documentation(request):
    return render(request,'Main_page/Documentation.html',context=documentationContext)

def TelegramBot(request):
    return render(request,'Main_page/TelegramBot.html',{'name_of_page': "TELEGRAM BOT"})
