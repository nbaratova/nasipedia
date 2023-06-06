"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5810711963:AAFX0BNl8OIjZeYNcHBHQMFoTECVYB1nNpI'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang('uz')


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Nasipediaga xush kelibsiz!")


@dp.message_handler()
async def get_summery(message: types.Message):
    try:
        summery = wikipedia.summary(message.text)
    except:
        await message.reply('Bunday maqola mavjud emas')

    await message.answer(summery)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
