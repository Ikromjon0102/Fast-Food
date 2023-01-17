from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ", "/start - Botni ishga tushirish", "/help - Yordam")

    await message.answer("\n".join(text))

@dp.message_handler(content_types='photo')
async def image_id(msg: types.Message):
    photo_id = msg.photo[-1].file_id
    await msg.answer(photo_id)