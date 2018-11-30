import os
from telegram.ext import Updater, CommandHandler


def suona(bot, update):
    update.message.reply_text("Hai suonato il citofono. Se sei all'ingresso 2 aspetta che qualcuno ti apra, se non lo sei vai e suona di nuovo.")
    os.popen('./ring.sh')

updater = Updater(os.environ['TOKEN'])

updater.dispatcher.add_handler(CommandHandler('suona', suona))

updater.start_polling()
updater.idle()

