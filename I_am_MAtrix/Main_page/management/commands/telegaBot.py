
from django.core.management.base import BaseCommand, CommandError
from I_am_MAtrix.settings import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        import telebot
        from telebot import types
        import time
        from threading import Thread

        bot = telebot.TeleBot(key)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markupHide = types.ReplyKeyboardRemove()


        markupInline = types.InlineKeyboardMarkup(row_width=3)

        def SendTo(message, answers, Aindex, Qindex, toMethod):
            markup.keyboard.clear()
            for i in answers[Aindex]:
                markup.add(i)
            bot.send_message(message.chat.id,qustions[Qindex], reply_markup=markup)
            bot.register_next_step_handler(message, toMethod)

        @bot.message_handler(commands=['start'])
        def start(message):
            global endList
            global programsTextList
            global programsText
            endList.clear()
            programsText = ""
            programsTextList.clear()

            markup.keyboard.clear()
            markup.add('Поехали!')
            bot.send_message(message.chat.id, str(start_chatting),reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def Dev(message):
            if(message.text.upper() == 'Поехали!'.upper()):
                bot.send_message(message.chat.id,'Круто!',reply_markup=markupHide)
                time.sleep(0.5)
                bot.send_message(message.chat.id,'Погнали!')
                time.sleep(0.5)
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
            priceS = 500000
            priceNS = 1000000
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
            global diagnostics
            global loading
            global aboutProgram
            global programsText
            
            def AddToShowList(message):
                global programsText
                showList = list()
                #bot.send_message(message.chat.id,'{}😋.'.format(endList),reply_markup=markupHide)
                #bot.send_message(message.chat.id,'{}😋.'.format(programsListForBot),reply_markup=markupHide)
                for i in programsListForBot:
                        if(endList[0] in programsListForBot[i][0] and endList[1] in programsListForBot[i][1] and endList[2] == programsListForBot[i][2] and endList[3] >= programsListForBot[i][3] and endList[4] in programsListForBot[i][4] and endList[5] in programsListForBot[i][5] and endList[6] in programsListForBot[i][6] and endList[7] in programsListForBot[i][7]):
                            showList.append(programsListForBot[i][8])
                for i in showList:
                    programsText += """{0}. {1}\n""".format(showList.index(str(i))+1,i)
                    programsTextList.append(i)


            def WriteText(message, text, b=False):
                if(b == False):
                    bot.send_message(message.chat.id,text)
                else:
                    bot.send_message(message.chat.id,text,reply_markup=markupHide)

            def InlineRequest(message):
                markupInline.keyboard.clear()
                for i in programsTextList:
                    markupInline.row(types.InlineKeyboardButton(str(programsTextList.index(i)+1), callback_data=i))
                    

            if(message.text == answers['prefabs'][0]):
                endList.append(ChooseProgramDict['prefabs'][0])
            elif(message.text == answers['prefabs'][1]):
                endList.append(ChooseProgramDict['prefabs'][1])                

            el1 = Thread(target=AddToShowList,args=(message,))
            el2 = Thread(target=InlineRequest,args=(message,))
            el1.start()
            el2.start()
            WriteText(message,diagnostics,True)
            time.sleep(1)
            WriteText(message,loading)
            time.sleep(0.7)
            bot.send_message(message.chat.id,{'Результаты:\n{}'.format(programsText)})
            time.sleep(2)
            bot.send_message(message.chat.id,aboutProgram,reply_markup=markupInline)
            CreateNewTableAboutUser(message.from_user.first_name,message.from_user.last_name,message.from_user.id,endList)
            #endList.clear()
            #programsText = ""
            #programsTextList.clear()
            #bot.send_message(message.chat.id,'{}😋.'.format(endList))
            #bot.send_message(message.chat.id,'{}😋.'.format(programsText))


        @bot.callback_query_handler(func=lambda call: True)
        def getNumblerOfProgram(call):
            global programsListForBot
            global programsTextList
            for i in programsListForBot:
                if(programsListForBot[i][8] == call.data):
                    bot.send_message(call.message.chat.id,programsListForBot[i][9])


        

        bot.polling(none_stop=True)
