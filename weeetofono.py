import os
# noinspection PyPackageRequirements
from telegram.ext import Updater, CommandHandler
import simpleaudio

campanello = None


# noinspection PyUnusedLocal
def suona(bot, update):
    global campanello
    update.message.reply_text("Hai suonato il citofono.\n\n\
Se sei all'ingresso 2 aspetta che qualcuno ti apra, se non lo sei vai e suona di nuovo.")
    # os.popen('./ring.sh')
    if campanello is not None and campanello.is_playing():
        campanello.stop()
    campanello = wave_obj.play()


wave_obj = simpleaudio.WaveObject.from_wave_file("weeedong.wav")

updater = Updater(os.environ['TOKEN'])

updater.dispatcher.add_handler(CommandHandler('suona', suona))

print("weeetofono started, begin polling")

updater.start_polling()
updater.idle()
