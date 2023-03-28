import re

from aiogram import types
from aiogram.dispatcher import FSMContext
import config
from loader import dp, bot


@dp.message_handler(commands='user_guide', state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("OK")
    await message.answer_document(document=config.FIRST_FILE)
    await message.answer_document(document=config.SECOND_FILE)
