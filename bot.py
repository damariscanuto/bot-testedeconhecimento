from telegram.ext import Updater,CommandHandler

def welcome(update, context):
    message = "Olá, " + update.message.from_user.first_name + "!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    token ='2068638050:AAHf3xx_gj6Isb2sXqE8JSiwG7-n8UTBnOY'
    updater = Updater(token=token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', welcome))
    updater.start_polling()
    print('teste'+ str(updater))
    updater.idle()
if __name__ == "__main__":
    main()