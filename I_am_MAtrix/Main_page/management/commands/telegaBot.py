
from django.core.management.base import BaseCommand, CommandError
from I_am_MAtrix.settings import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        import telebot
        from telebot import types
        import time

        bot = telebot.TeleBot(key)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markupHide = types.ReplyKeyboardRemove()

        def SendTo(message, answers, Aindex, Qindex, toMethod):
            markup.keyboard.clear()
            for i in answers[Aindex]:
                markup.add(i)
            bot.send_message(message.chat.id,qustions[Qindex], reply_markup=markup)
            bot.register_next_step_handler(message, toMethod)

        @bot.message_handler(commands=['start'])
        def start(message):
            markup.keyboard.clear()
            markup.add('Поехали!')
            bot.send_message(message.chat.id, str(start_chatting),reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def Dev(message):
            if(message.text.upper() == 'Поехали!'.upper()):
                bot.send_message(message.chat.id,'Круто!',reply_markup=markupHide)
                bot.send_message(message.chat.id,'Погнали!')
                markup.keyboard.clear()
                markup.add(answers['devices'][1],answers['devices'][2])
                markup.add(answers['devices'][0])
                bot.send_message(message.chat.id,qustions[0], reply_markup=markup,)
                bot.register_next_step_handler(message, Cost)
            else:
                bot.send_message(message.chat.id,'Напишите /start, чтобы начать.')
                
        def Cost(message):
            global endList
            global ChooseProgramDict
            if(message.text == answers['devices'][0]):
                endList.append(ChooseProgramDict['devices'][0])
                SendTo(message,answers,'cost',1,Using)
            elif(message.text == answers['devices'][1]):
                endList.append(ChooseProgramDict['devices'][1])
                SendTo(message,answers,'cost',1,Using)
            elif(message.text == answers['devices'][2]):
                endList.append(ChooseProgramDict['devices'][2])
                SendTo(message,answers,'cost',1,Using)

        def Using(message):
            global endList
            global ChooseProgramDict
            def ToChoosePrice(price):
                markup.keyboard.clear()
                bot.send_message(message.chat.id,price,reply_markup=markupHide) 
                bot.register_next_step_handler(message, ChoosePrice)

            if(message.text == answers['cost'][0]):
                endList.append(ChooseProgramDict['cost'][0])
                endList.append(ChooseProgramDict['subscription'][1])
                endList.append(ChooseProgramDict['pay'][0])
                SendTo(message,answers,'using',2,Type)
            elif(message.text == answers['cost'][1]):
                endList.append(ChooseProgramDict['cost'][1])
                endList.append(ChooseProgramDict['subscription'][1])
                ToChoosePrice(price)
            elif(message.text == answers['cost'][2]):
                endList.append(ChooseProgramDict['cost'][1])
                endList.append(ChooseProgramDict['subscription'][0])
                ToChoosePrice(priceSubscribe)

        def ChoosePrice(message):
            global ChooseProgramDict
            global endList
            priceS = 180000
            priceNS = 200000
            if(endList[2] == True):
                try:
                    if(int(message.text) > 0):
                        if(int(message.text) < priceS):
                            endList.append(int(message.text))
                            SendTo(message,answers,'using',2,Type)
                        elif( int(message.text) > priceS):
                            bot.send_message(message.chat.id,'Введите пожалуйста сумму менее {}.'.format(priceS))
                            bot.register_next_step_handler(message, ChoosePrice)
                    elif(int(message.text) <= 0):
                        bot.send_message(message.chat.id,'Введите пожалуйста сумму более 0.')
                        bot.register_next_step_handler(message, ChoosePrice)
                except Exception:
                    bot.send_message(message.chat.id,'Введите пожалуйста число.')
                    bot.register_next_step_handler(message, ChoosePrice)
            elif(endList[2] == False):
                try:
                    if(int(message.text) > 0):
                        if(int(message.text) < priceNS):
                            endList.append(int(message.text))
                            SendTo(message,answers,'using',2,Type)
                        elif( int(message.text) > priceNS):
                            bot.send_message(message.chat.id,'Введите пожалуйста сумму менее {}.'.format(priceNS))
                            bot.register_next_step_handler(message, ChoosePrice)
                    elif(int(message.text) <= 0):
                        bot.send_message(message.chat.id,'Введите пожалуйста сумму более 0.')
                        bot.register_next_step_handler(message, ChoosePrice)
                except Exception:
                    bot.send_message(message.chat.id,'Введите пожалуйста число.')
                    bot.register_next_step_handler(message, ChoosePrice)

        def Type(message):
            global ChooseProgramDict
            global endList
            if(message.text == answers['using'][0]):
                endList.append(ChooseProgramDict['using'][0])
                SendTo(message,answers,'type',3,Experience)
            elif(message.text == answers['using'][1]):
                endList.append(ChooseProgramDict['using'][1])
                SendTo(message,answers,'type',3,Experience)
            elif(message.text == answers['using'][2]):
                endList.append(ChooseProgramDict['using'][2])
                SendTo(message,answers,'type',3,Experience)

        def Experience(message):
            global ChooseProgramDict
            global endList
            if(message.text == answers['type'][0]):
                endList.append(ChooseProgramDict['typeOfModeling'][0])
                SendTo(message,answers,'experience',4,Prefabs)
            elif(message.text == answers['type'][1]):
                endList.append(ChooseProgramDict['typeOfModeling'][1])
                SendTo(message,answers,'experience',4,Prefabs)
            elif(message.text == answers['type'][2]):
                endList.append(ChooseProgramDict['typeOfModeling'][2])
                SendTo(message,answers,'experience',4,Prefabs)

        def Prefabs(message):
            global ChooseProgramDict
            global endList
            if(message.text == answers['experience'][0]):
                endList.append(ChooseProgramDict['experience'][0])
                SendTo(message,answers,'prefabs',5,End)
            elif(message.text == answers['experience'][1]):
                endList.append(ChooseProgramDict['experience'][1])
                SendTo(message,answers,'prefabs',5,End)

        def End(message):
            global ChooseProgramDict
            global endList
            
            if(message.text == answers['prefabs'][0]):
                endList.append(ChooseProgramDict['prefabs'][0])
            elif(message.text == answers['prefabs'][1]):
                endList.append(ChooseProgramDict['prefabs'][1])
            bot.send_message(message.chat.id,'{}😋.'.format(endList),reply_markup=markupHide)
            bot.send_message(message.chat.id,'{}😋.'.format(programsListForBot),reply_markup=markupHide)
            for i in programsListForBot:
                    if(endList[0] in programsListForBot[i][0] and endList[1] in programsListForBot[i][1] and endList[2] == programsListForBot[i][2] and endList[3] >= programsListForBot[i][3] and endList[4] in programsListForBot[i][4] and endList[5] in programsListForBot[i][5] and endList[6] in programsListForBot[i][6] and endList[7] in programsListForBot[i][7]):
                        bot.send_message(message.chat.id,programsListForBot[i][8])


            endList.clear()
            bot.send_message(message.chat.id,'{}😋.'.format(endList))
        
        bot.polling(none_stop=True)
