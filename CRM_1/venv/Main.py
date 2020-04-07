import telebot
import botinfo
import logging
import datetime
import req
from Read_info import *
import DbContext

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot = telebot.TeleBot(botinfo.TOKEN)

is_listen=False

@bot.message_handler(commands=["start"])
def handler_start(message):
	global is_listen
	bot.send_message(message.chat.id," Hello! Send me contact information like this:\nPhone Number : +38xxxxxxxxx\n Name : xxxxx")
	is_listen=True
@bot.message_handler()
def handler_get_info(message):
	global is_listen
	if is_listen==True:
		mes = search(message.text)
		response=req.restCreate(mes)
		#DELETE THIS ON RELEASE!
		DbContext.write_response(response)
		# DELETE THIS ON RELEASE!
		bot.send_message(message.chat.id,
					 "Ok!")
		is_listen=False
bot.polling()

