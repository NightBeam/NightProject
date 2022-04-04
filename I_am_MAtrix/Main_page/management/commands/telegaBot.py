
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
            if(message.text == answers['devices'][0]):
                SendTo(message,answers,'cost',1,Using)
            elif(message.text == answers['devices'][1]):
                SendTo(message,answers,'cost',1,Using)
            elif(message.text == answers['devices'][2]):
                SendTo(message,answers,'cost',1,Using)

        def Using(message):
            def ToChoosePrice(price):
                markup.keyboard.clear()
                bot.send_message(message.chat.id,price,reply_markup=markupHide) 
                bot.register_next_step_handler(message, ChoosePrice)

            if(message.text == answers['cost'][0]):
                SendTo(message,answers,'using',2,Type)
            elif(message.text == answers['cost'][1]):
                ToChoosePrice(price)
            elif(message.text == answers['cost'][2]):
                global subscription
                subscription = True
                ToChoosePrice(priceSubscribe)

        def ChoosePrice(message):
            global subscription
            priceS = 150000
            priceNS = 200000
            if(subscription == True):
                try:
                    if(int(message.text) > 0):
                        if(int(message.text) < priceS):
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
            elif(subscription == False):
                try:
                    if(int(message.text) > 0):
                        if(int(message.text) < priceNS):
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
            if(message.text == answers['using'][0]):
                SendTo(message,answers,'type',3,Experience)
            elif(message.text == answers['using'][1]):
                SendTo(message,answers,'type',3,Experience)
            elif(message.text == answers['using'][2]):
                SendTo(message,answers,'type',3,Experience)

        def Experience(message):
            if(message.text == answers['type'][0]):
                SendTo(message,answers,'experience',4,Prefabs)
            elif(message.text == answers['type'][1]):
                SendTo(message,answers,'experience',4,Prefabs)
            elif(message.text == answers['type'][2]):
                SendTo(message,answers,'experience',4,Prefabs)

        def Prefabs(message):
            if(message.text == answers['experience'][0]):
                SendTo(message,answers,'prefabs',5,End)
            elif(message.text == answers['experience'][1]):
                SendTo(message,answers,'prefabs',5,End)

        def End(message):
            if(message.text == message.text):
                bot.send_message(message.chat.id,'{} - ты пидор😋.'.format(message.from_user.first_name),reply_markup=markupHide)
        
        bot.polling(none_stop=True)
