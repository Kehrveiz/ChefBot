import src.config as config

from .bot import bot
from ..logic import get_response


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    if message.chat.type == "private":

        bot.reply_to(message, "Mensaje de Bienvenida")


@bot.message_handler(func = lambda m: m.chat.type == "private")
def echo_all(message):
	bot.send_message(message.chat.id, get_response(message.text))
