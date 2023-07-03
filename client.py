import random
import pers
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

import admins
import tok
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sql_db
import keyboard_main
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


temp_code = {}


class Bron(StatesGroup):
    sost1 = State()


async def bron1(message: types.Message):
    await message.reply("Введите желаемые день и время посещения нашего заведения, зал, в которомы вы "
                        "желаете расположиться (в одном сообщении). "
                        "Для отмены бронирования нажмите кнопку 'Отмена'",
                        reply_markup=keyboard_main.kb_zakaz)
    await Bron.sost1.set()


async def bron2(message : types.Message, state = FSMContext):
    bron = await sql_db.bron(message)
    await state.finish()
    master = await sql_db.master()
    await bot.send_message(master[0], f"номер {bron[0][0][0]} @{bron[3][0][0]} ,бронь на {bron[1][0][0]} ")
    await message.reply("В ближайшее время вам поступит ответ по вашему бронированию",
                        reply_markup=keyboard_main.ikb_uslugi)


async def cancel(message : types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK")

@dp.message_handler(lambda message: message.text.lower() in ["кто на смене?", '/master'])
async def masters(message: types.Message):
    master = await sql_db.master()
    await bot.send_photo(message.from_user.id, f"{master[1]}")
    await bot.send_message(message.from_user.id, f"На смене рулит всем {master[2]}", reply_markup=keyboard_main.ikb_main)



@dp.message_handler(lambda message: message.text == "Ознакомиться с отзывами")
async def read_tells(message: types.Message):
    tells: list = await sql_db.tells_of_another()
    await bot.send_message(message.from_user.id, f"Отзыв о нашем кафе:\n"
                                                 f">>{random.choice(tells)}<<", reply_markup=keyboard_main.ikb_tells)


@dp.callback_query_handler(text="next_tell")
async def read_tells(cb: types.CallbackQuery):
    tells: list = await sql_db.tells_of_another()
    await bot.edit_message_text(message_id=cb.message.message_id, chat_id=cb.message.chat.id, text=f"Отзыв о нашем кафе:\n"
                                f">>{random.choice(tells)}<<", reply_markup=keyboard_main.ikb_tells)


class Tell(StatesGroup):
    sost1 = State()

async def tell1(message: types.Message):
    await message.reply("Введите текст отзыва о нашем кафе(в одном сообщении). "
                        "Для отмены бронирования нажмите кнопку 'Отмена'",
                        reply_markup=keyboard_main.ikb_cancel)
    await Tell.sost1.set()


async def tell2(message : types.Message, state = FSMContext):
    await sql_db.tells_to_base(message)
    await state.finish()
    max = await sql_db.get_max_tell()
    ib_code = InlineKeyboardButton(text="Дать код", callback_data=f"code = {max}")
    ib_bad_tell = InlineKeyboardButton(text="Очень плохой отзыв", callback_data=f"tell = {max}")
    ikb_code = InlineKeyboardMarkup(row_width=1).row(ib_code).row(ib_bad_tell)
    for i in pers.amdins:
        try:
            await bot.send_message(i, f"Поступил отзыв\n{message.text}", reply_markup=ikb_code)
        except:
            pass
    await message.reply("Спасибо за Ваш отзыв")




def registr_client(dp: Dispatcher):
    dp.register_message_handler(bron1, lambda message: message.text in ["Забронировать стол", "/reservation"], state=None)
    dp.register_message_handler(tell1, lambda message: message.text == "Оставить отзыв", state=None)
    dp.register_message_handler(cancel, state="*", commands=['отмена', 'cancel'])
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(bron2, state=Bron.sost1)
    dp.register_message_handler(tell2, state=Tell.sost1)