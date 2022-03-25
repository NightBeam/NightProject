
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        import telebot
        from telebot import types

        bot = telebot.TeleBot("1857719214:AAFdr9bYxDlQiLKDi6otg8CGcWfJPHJOAnk")

        start_chatting = """Привет! Я GIDA BOT, виртуальный ассистент, специализирующийся на 3D-моделировании.
        Если ты пройдешь небольшой тест, то я смогу подобрать программу для тебя!
        Чтобы начать тест, нажми "Поехади"! """


        @bot.message_handler(commands=['start'])
        def start(message):
            markup = types.InlineKeyboardMarkup()
            Go = types.InlineKeyboardButton('Поехали', callback_data='go')
            No = types.InlineKeyboardButton('Не интересует', callback_data='no')

            markup.add(Go, No)
            bot.send_message(message.chat.id, str(start_chatting),reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def handle(call):
            if(call.data == "go"):
                bot.send_message(call.message.chat.id,"ok, let's go")
            elif(call.data == "no"):
                bot.send_message(call.message.chat.id,"baaad, fuuck you")
            bot.answer_callback_query(call.id)


        bot.polling(none_stop=True)
