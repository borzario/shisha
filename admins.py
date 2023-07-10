from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sql_db
import keyboard_main
import pers
import random


@dp.message_handler(lambda message: message.text.lower() in ["я на смене", "/atwork"])
async def smena(message: types.Message):
    await bot.send_message(message.from_user.id, "Красава, братиш!!", reply_markup=keyboard_main.kb_mainwindow_admin)
    await sql_db.set_master(message)


class Brona(StatesGroup):
    sosta = State()
    s_no = State()

async def brona(message: types.Message):
    await bot.send_message(message.from_user.id, "бро, введи номер брони")
    await Brona.sosta.set()


async def brona_no(message: types.Message):
    await bot.send_message(message.from_user.id, "бро, введи номер брони")
    await Brona.s_no.set()

async def bronb(message: types.Message, state=FSMContext):
    user = await sql_db.bronselect(message)
    await bot.send_message(message.from_user.id, "Клиент уведомлен о подтверждении брони")
    await state.finish()
    await bot.send_message(user[0][0], "Столик забронирован, ждем вас")

async def bronb_no(message: types.Message, state=FSMContext):
    user = await sql_db.bronselect(message)
    await bot.send_message(message.from_user.id, "Клиент уведомлен об отказе в брони")
    await state.finish()
    await bot.send_message(user[0][0], "Бронь не подтверждена. Выберите другое время")



async def cancel(message : types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK")


class Spam(StatesGroup):
    sost1 = State()
    sost2 = State()

async def spam(messsage: types.Message):
    await bot.send_message(messsage.from_user.id, "братка, введи текст рассылки")
    await Spam.sost1.set()


async def spam1(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["text"] = message.text
    await bot.send_message(message.from_user.id, "Отправь фото для рассылки")
    await Spam.sost2.set()
    await bot.send_message(message.from_user.id, "Spam was sended ;)")


async def spam3(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await sql_db.spam(data)
    await state.finish()


@dp.callback_query_handler(lambda i: i.from_user.id in pers.amdins and i.data.startswith("code"))
async def unz(cb: types.CallbackQuery):
    code = int(cb.data[7:])
    user = await sql_db.get_user_tell(code)
    promo_dict: str = "123456789ABCDFG"
    promo = "".join(random.choices(promo_dict, k=4))
    if user not in await sql_db.get_all_users_with_code_tell():
        await bot.send_message(user, f"Ваш отзыв принят, спасибо!\nПромокод на бесплатный кофе - {promo}",
                               reply_markup=keyboard_main.ikb_main)
        await sql_db.give_code(user, promo)
        await bot.send_message(cb.from_user.id, "Code was sended to client")
    else:
        await bot.send_message(cb.from_user.id, "this user had get code early")


@dp.callback_query_handler(lambda i: i.from_user.id in pers.amdins and i.data.startswith("tell"))
async def unz(cb: types.CallbackQuery):
    code = int(cb.data[7:])
    await sql_db.change_to_bad(code, cb.from_user.id)



def registr_admin(dp: Dispatcher):
    dp.register_message_handler(brona, lambda message: "Подтвердить бронь" in message.text, state=None)
    dp.register_message_handler(brona_no, lambda message: "отменить бронь" in message.text, state=None)
    dp.register_message_handler(spam, lambda message: "Запилить рассылку" in message.text, state=None)
    dp.register_message_handler(cancel, state="*", commands='отмена')
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(spam1, state=Spam.sost1)
    dp.register_message_handler(spam3, content_types = ['photo'], state=Spam.sost2)
    dp.register_message_handler(bronb, state=Brona.sosta)
    dp.register_message_handler(bronb_no, state=Brona.s_no)