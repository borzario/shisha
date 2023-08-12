import random
import pers
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram_calendar import simple_cal_callback, SimpleCalendar
import admins
import tok
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sql_db
import keyboard_main
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from datetime import timedelta, date, datetime

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
    await bot.send_message(master, f"номер {bron[0][0][0]} @{bron[3][0][0]} ,бронь на {bron[1][0][0]} ")
    await message.reply("В ближайшее время вам поступит ответ по вашему бронированию",
                        reply_markup=keyboard_main.ikb_uslugi)


async def cancel(message : types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.from_user.id, "ОК")

@dp.message_handler(lambda message: message.text.lower() in ["кто на смене?", '/master'])
async def masters(message: types.Message):
    master = int(await sql_db.master())
    await bot.send_photo(message.from_user.id, f"{pers.masters[master][1]}")
    await bot.send_message(message.from_user.id, f"Сегодня дымным процессом рулит {pers.masters[master][0]}",
                           reply_markup=keyboard_main.ikb_main)



@dp.message_handler(lambda message: message.text == "Ознакомиться с отзывами")
async def read_tells(message: types.Message):
    tells: list = await sql_db.tells_of_another()
    await bot.send_message(message.from_user.id, f"Отзыв о нашем launge баре:\n"
                                                 f">>{random.choice(tells)}<<", reply_markup=keyboard_main.ikb_tells)


@dp.callback_query_handler(text="next_tell")
async def read_tells(cb: types.CallbackQuery):
    tells: list = await sql_db.tells_of_another()
    await bot.edit_message_text(message_id=cb.message.message_id, chat_id=cb.message.chat.id, text=f"Отзыв о нашем launge баре:\n"
                                f">>{random.choice(tells)}<<", reply_markup=keyboard_main.ikb_tells)


class Tell(StatesGroup):
    sost1 = State()

async def tell1(message: types.Message):
    await message.reply("Введите текст отзыва о нашем launge баре(в одном сообщении). "
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


class Rent(StatesGroup):
    fam = State()
    name = State()
    sname = State()
    bday = State()
    reg = State()
    pasp = State()
    photo = State()
    date_first = State()
    date_sec = State()
    tel = State()
    adres_dost = State()
    kem = State()


@dp.callback_query_handler(text="with_dost")
async def rent_hookah(cb: types.CallbackQuery):
    await bot.send_message(cb.from_user.id, "Отправьт боту вашу фамилию", reply_markup=keyboard_main.ikb_cancel)
    await Rent.fam.set()


@dp.message_handler(state=Rent.fam)
async def set_fam(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["fam"] = message.text
        data["user"] = message.from_user.id
    await bot.send_message(message.from_user.id, "Отправьт боту ваше имя", reply_markup=keyboard_main.ikb_cancel)
    await Rent.name.set()


@dp.message_handler(state=Rent.name)
async def set_name(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await bot.send_message(message.from_user.id, "Отправьт боту ваше отчество", reply_markup=keyboard_main.ikb_cancel)
    await Rent.sname.set()


@dp.message_handler(state=Rent.sname)
async def set_sname(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["sname"] = message.text
    await bot.send_message(message.from_user.id, "Отправьт боту вашу дату рождения в формате чч.мм.гггг",
                           reply_markup=keyboard_main.ikb_cancel)

    await Rent.bday.set()


@dp.message_handler(state=Rent.bday)
async def set_bday(message: types.Message, state = FSMContext):
    try:
        if (int(message.text[-4:]) > 2005) or ((int(message.text[-4:]) == 2005) and (int(message.text[3:5]) > 7)):
            await bot.send_message(message.from_user.id, "Табачные изделия и принадлежность допускаются к обороту для лиц "
                                                          "старше  18 лет")
            await state.finish()
    except:
        async with state.proxy() as data:
            data["bday"] = message.text
        await bot.send_message(message.from_user.id, "Отправьт боту адрес вашей регистрации (одним сообщением)",
                                                                reply_markup=keyboard_main.ikb_cancel)
        await Rent.reg.set()


@dp.message_handler(state=Rent.reg)
async def set_reg(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["reg"] = message.text
    await bot.send_message(message.from_user.id, "Отправьте боту кем выдан паспорт (одним сообщением)",
                           reply_markup=keyboard_main.ikb_cancel)
    await Rent.kem.set()


@dp.message_handler(state=Rent.kem)
async def set_reg(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["pasp"] = message.text
    await bot.send_message(message.from_user.id, "Отправьте боту серию и номер паспорта (одним сообщением)",
                           reply_markup=keyboard_main.ikb_cancel)
    await Rent.pasp.set()

@dp.message_handler(state=Rent.pasp)
async def set_pasp(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["kem"] = message.text
    await bot.send_message(message.from_user.id, "Отправьте боту фото документа, подтврждающего введенные данные (система"
                                                 "не хранит изображения ваших документов)",
                           reply_markup=keyboard_main.ikb_cancel)
    await Rent.photo.set()


@dp.message_handler(content_types = ['photo'], state=Rent.photo)
async def set_photo(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await bot.send_message(message.from_user.id, 'Выберите дату получения кальяна:',
                           reply_markup=await SimpleCalendar().start_calendar())
    await Rent.date_first.set()


@dp.callback_query_handler(simple_cal_callback.filter(), state=Rent.date_first)
async def process_select_start_date(cb: types.CallbackQuery, callback_data: dict, state=FSMContext) -> None:
    selected, date = await SimpleCalendar().process_selection(cb, callback_data)
    if selected:
        async with state.proxy() as data:
            data["fdate"] = date
            await Rent.date_sec.set()
            await bot.send_message(cb.from_user.id, 'Выберите дату сдачи кальяна:',
                                   reply_markup=await SimpleCalendar().start_calendar())


@dp.callback_query_handler(simple_cal_callback.filter(), state=Rent.date_sec)
async def process_select_end_date(cb: types.CallbackQuery, callback_data: dict, state=FSMContext) -> None:
    """ Процесс выбора начального времени поиска """
    selected, date_n = await SimpleCalendar().process_selection(cb, callback_data)
    if selected:
        async with state.proxy() as data:
            data["sdate"] = date_n
            def daterange(date1: datetime, date2):
                for n in range(int((date2 - date1).days) + 1):
                    yield date1 + timedelta(n)
            data["days"] = [i for i in daterange(data["fdate"], data["sdate"])]
    await bot.send_message(cb.from_user.id, 'Введите ваш номер телефона', reply_markup=keyboard_main.ikb_cancel)
    await Rent.tel.set()

@dp.message_handler(state=Rent.tel)
async def set_tel(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["tel"] = message.text
    await bot.send_message(message.from_user.id, "Укажите адрес доставки (в одном сообщении)",
                           reply_markup=keyboard_main.ikb_cancel)
    await Rent.adres_dost.set()


@dp.message_handler(state=Rent.adres_dost)
async def set_adr_d(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data["adr_d"] = message.text
        await sql_db.add_text(data)
        master = await sql_db.master()
        await bot.send_document(master, InputFile(f"data_base/texts/Договор аренды {data['user']}.docx"))
        await bot.send_message(master, f"Заказ на аренду кальна от {data['fam']} {data['name']} с {data['fdate']}"
                                          f" по {data['sdate']}. Адрес доставки - {data['adr_d']}. Телефон для связи - "
                                          f"{data['tel']}. Бро, сверь фото документа с данными в договоре.")
        await bot.send_photo(master, data["photo"])
    await bot.send_message(message.from_user.id, "Заказ оформлен",
                           reply_markup=keyboard_main.ikb_main)
    await state.finish()


def registr_client(dp: Dispatcher):
    dp.register_message_handler(bron1, lambda message: message.text in ["Забронировать стол", "/reservation"], state=None)
    dp.register_message_handler(tell1, lambda message: message.text == "Оставить отзыв", state=None)
    dp.register_message_handler(cancel, state="*", commands=['отмена', 'cancel'])
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_callback_query_handler(cancel, text="cancel", state="*")
    dp.register_message_handler(bron2, state=Bron.sost1)
    dp.register_message_handler(tell2, state=Tell.sost1)