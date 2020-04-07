import telebot
import config
import dbworker
import UsersDB
import req

bot = telebot.TeleBot(config.token)

# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, " Hello! Send me your ID!")

    dbworker.set_state(message.chat.id, config.States.S_ENTER_ID.value)

# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "...")
    dbworker.set_state(message.chat.id, config.States.S_ENTER_ID.value)
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_ID.value)
def user_entering_name(message):
    # В случае с именем не будем ничего проверять, пусть хоть "25671", хоть Евкакий
    bot.send_message(message.chat.id, "OK! Send your question")
    UsersDB.setNewUser(message.from_user, message.text)
    dbworker.set_state(message.chat.id, config.States.S_ENTER_QUESTION.value)
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_QUESTION.value)
def user_entering_name(message):
    # В случае с именем не будем ничего проверять, пусть хоть "25671", хоть Евкакий
    bot.send_message(message.chat.id, "OK! I`ll get it")
    UsersDB.addQuestion(message.from_user, message.text)

    res=req.restCreate(message.from_user)
    
    dbworker.set_state(message.chat.id, config.States.S_START.value)
    UsersDB.delinfo(message.from_user)
bot.polling(none_stop=True)