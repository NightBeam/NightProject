from django.shortcuts import render, HttpResponse


game_info = [{"game" : {"name":"Fruit Fight","link": "#"}}]
ourGamesContext =  {"name_of_page": "OUR GAMES","games" : game_info}




# Create your views here.
def AboutUs(request):
    return render(request,'Main_page/AboutUs.html',{'name_of_page': "ABOUT US"})

def OurWorks(request):
    return render(request,'Main_page/OurWorks.html',{'name_of_page': "OUR WORKS"})

def OurGames(request):
    return render(request,'Main_page/OurGames.html',context=ourGamesContext)
def Statistics(request):
    return render(request,'Main_page/Statistics.html',{'name_of_page': "STATISTICS"})

def Documentation(request):
    return render(request,'Main_page/Documentation.html',{'name_of_page': "DOCUMENTATION"})

def TelegramBot(request):
    return render(request,'Main_page/TelegramBot.html',{'name_of_page': "TELEGRAM BOT"})
