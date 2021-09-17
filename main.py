from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, updater
from api import *
import logging
import json

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)
with open('data.json', 'r') as file:
    data = json.load(file)


def main():
    updater = Updater(token=data["token"], use_context=True)
    dp = updater.dispatcher



    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('git', version))

    dp.add_handler(CommandHandler('tts', tts, pass_args=True))
    dp.add_handler(CommandHandler('ttsCn', ttsCn, pass_args=True))
    dp.add_handler(CommandHandler('ttsArb', ttsArb, pass_args=True))
    dp.add_handler(CommandHandler('ttsFr', ttsFr, pass_args=True))
    dp.add_handler(CommandHandler('ttsJp', ttsJp, pass_args=True))
    dp.add_handler(CommandHandler('ttsMx', ttsMx, pass_args=True))
    dp.add_handler(CommandHandler('ttsRu', ttsRu, pass_args=True))


    print('[ ! ] Initializing bot ...')
    updater.start_polling()
    print('[ ok ] Bot is running ...')


if __name__ == '__main__':
    main()