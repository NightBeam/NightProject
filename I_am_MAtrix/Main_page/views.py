from django.shortcuts import render, HttpResponse, redirect
from .models import *

infaAU = InfaAboutUs.objects.all()
videoOW = VideoOurWorks.objects.all()
datasDOC = ProgramsInfa.objects.all()
datasWeAre = We.objects.all()
datasTypeOfModeling = TypeOfModeling.objects.all()
datasOfUser = ChoiseOfUser.objects.all()
datasTOM = list()
datasUsing = list()
datasTOM.append(int(datasTypeOfModeling[0].number))
datasTOM.append(int(datasTypeOfModeling[1].number))
datasTOM.append(int(datasTypeOfModeling[2].number))
datasUsing.append(int(datasTypeOfModeling[3].number))
datasUsing.append(int(datasTypeOfModeling[4].number))
datasUsing.append(int(datasTypeOfModeling[5].number))
datasTOMB = [0,0,0]
for i in datasOfUser:
    if("Solid" in i.choise):
        datasTOMB[0] += 1
    elif("Polygonal" in i.choise):
        datasTOMB[1] += 1
    elif("Sculpting" in i.choise):
        datasTOMB[1] += 1
datasUsingB = [0,0,0]
for i in datasOfUser:
    if("Series" in i.choise):
        datasUsingB[0] += 1
    elif("VideoGames" in i.choise):
        datasUsingB[1] += 1
    elif("Models" in i.choise):
        datasUsingB[2] += 1


game_info = [{"game" : {"name":"Fruit Fight","link": "#"}}]
ourGamesContext =  {"name_of_page": "ИГРЫ","games" : game_info}
aboutUsContext = {'name_of_page': "О НАС", 'paragraphs': infaAU,'weAre':datasWeAre}
ourWorksContext = {"name_of_page": "НАШИ РАБОТЫ",'videoOfWorks': videoOW}
documentationContext = {'name_of_page':"ДОКУМЕНТАЦИЯ", 'programs':datasDOC}
statisticsContext = {'name_of_page':"СТАТИСТИКА",'typeOfModeling':datasTOM,'typeOfModelingTB':datasTOMB,'UsingTB':datasUsingB,'Using':datasUsing}
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
