from aiogram.types import InputMediaPhoto
from aiogram.utils import executor
import pers
import admins
import photos
from create_bot import dp, bot
from aiogram import types
import keyboard_main
from data_base import sql_db
from client import *
from admins import *
import zakazaka

async def on_startup(_):
    print("Папа в здании")
    sql_db.db_start()


temp_user = {}


@dp.callback_query_handler(text="в начало")
@dp.message_handler(lambda message: message.text.lower() in ["в начало", '/main'])
async def salam(message: types.Message):
    """await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIHRGMLJhCchUeJOxUi85ASQ0wy1pXOAAKNqjEbh4xZRN1YiXXKQzlcAQADAgADcwADKQQ")"""
    if message.from_user.id in pers.amdins:
        await bot.send_message(message.from_user.id, "Салам, родная",
                               reply_markup=keyboard_main.kb_mainwindow_admin)
    else:
        await bot.send_message(message.from_user.id, "Выберите категорию",
                               reply_markup=keyboard_main.kb_mainwindow)

@dp.message_handler(lambda message: "start" in message.text.lower())
async def start(message: types.Message):
    #await bot.send_video(message.from_user.id, "BAACAgIAAxkBAAIKJmMLfIUGuimxS-DTlsb5cqSr1WsdAAL0IwAC5RZQSC7-V5eS635sKQQ")
    if message.from_user.id in pers.amdins:
        await bot.send_message(message.from_user.id, "Салам, родная",
                               reply_markup=keyboard_main.kb_mainwindow_admin)
    else:
        await bot.send_message(message.from_user.id, "Здравствуйте, дорогой друг!\nВыберитe категорию, нажав на соответствующую кнопку",
                               reply_markup=keyboard_main.kb_mainwindow)
        await sql_db.user_add(message)

@dp.message_handler(lambda message: "контакты" in message.text.lower())
async def kontakts(message: types.Message):
    await bot.send_message(message.from_user.id, "Телефон нашего кафе - +79900691693", reply_markup=keyboard_main.ikb_main)

@dp.message_handler(lambda message: "адрес" in message.text.lower())
async def adress(message: types.Message):
    await bot.send_message(message.from_user.id, "Наше кафе расположено по адресу: г. Скадовск, "
                                                 "ул. Сергеевская, д. 11", reply_markup=keyboard_main.ikb_main)

@dp.message_handler(lambda message: "режим работы" in message.text.lower())
async def time(message: types.Message):
    await bot.send_message(message.from_user.id, "Наше кафе открыто для гостей ежедневно с 09.00 до 19.00", reply_markup=keyboard_main.ikb_main)

@dp.callback_query_handler(text="О нашем кафе")
@dp.message_handler(lambda message: "о нашем кафе" in message.text.lower())
async def about(message: types.Message):
    await bot.send_message(message.from_user.id, "В нашем заведении всегда царит дружеская атмосфера.\n Вы можете ознакомиться "
                                                 "интерьером зала, узнать наш адрес, время работы, телефон для связи.", reply_markup=keyboard_main.kb_ourbar)
    await bot.send_message(message.from_user.id,
                           text="Выберите категорию", reply_markup=keyboard_main.ikb_main)



@dp.message_handler(lambda message: "интерьер" in message.text.lower())
async def interier(message: types.Message):
    temp_user[message.from_user.id] = temp_user.get(message.from_user.id, 0)
    photo_number: int = temp_user[message.from_user.id]
    await bot.send_photo(message.from_user.id, photos.rooms[photo_number], reply_markup=keyboard_main.ikb_about)
    temp_user[message.from_user.id] = (temp_user.get(message.from_user.id, 0) + 1) % 6


@dp.callback_query_handler(text="next_photo")
async def interier2(cb: types.CallbackQuery):
    temp_user[cb.from_user.id] = temp_user.get(cb.from_user.id, 0)
    photo_number: int = temp_user[cb.from_user.id]
    photo_file = InputMediaPhoto(photos.rooms[photo_number])
    await bot.edit_message_media(media=photo_file, message_id=cb.message.message_id,
                                 chat_id=cb.message.chat.id, reply_markup=keyboard_main.ikb_about)
    temp_user[cb.from_user.id] = (temp_user.get(cb.from_user.id, 0) + 1) % 6



@dp.message_handler(lambda message: "наши мастера" in message.text.lower())
async def masters(message: types.Message):
    await bot.send_message(message.from_user.id, "Наши доблестные мастера кальянного дела", reply_markup=
                           keyboard_main.kb_who_at_work)
    """await bot.send_photo(message.from_user.id,
                         "AgACAgEAAxkBAAIH82MLNtpvLh0qdVsz8OgqwX5YYSRXAAKfqjEbh4xZRGhiN7Q_NpHPAQADAgADcwADKQQ")"""


@dp.callback_query_handler(text="Услуги нашего заведения")
@dp.message_handler(lambda message: "услуги нашего заведения" in message.text.lower())
async def positions(message: types.Message):
    await bot.send_message(message.from_user.id, "Дорогой друг, выберите категорию", reply_markup=keyboard_main.kb_uslugi)
    await bot.send_message(message.from_user.id,
                           text="Выберите категорию", reply_markup=keyboard_main.ikb_main)


@dp.message_handler(lambda message: "кальянные радости" in message.text.lower())
async def hookah(message: types.Message):
    await bot.send_message(message.from_user.id, "Дымное удовольствие на любой вкус.")
    await bot.send_photo(message.from_user.id, photos.hookah, reply_markup=keyboard_main.ikb_main)


@dp.callback_query_handler(lambda c: "menu" in c.data)
@dp.message_handler(lambda message: "меню" in message.text.lower())
async def manu(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["menu"])
    await bot.send_message(message.from_user.id, "Выберите категорию", reply_markup=keyboard_main.kb_menu)


@dp.message_handler(lambda message: "закуски" in message.text.lower())
async def zakus(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["zakus"], reply_markup=keyboard_main.ikb_z_zakus)



@dp.message_handler(lambda message: "салаты" in message.text.lower())
async def salat(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["salat"], reply_markup=keyboard_main.ikb_z_salat)


@dp.message_handler(lambda message: "напитки" in message.text.lower())
async def drink(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["drink"], reply_markup=keyboard_main.ikb_z_drink)


@dp.message_handler(lambda message: "завтраки" in message.text.lower())
async def hookah(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["brekfast"], reply_markup=keyboard_main.ikb_z_brekf)


@dp.message_handler(lambda message: "горячие блюда" in message.text.lower())
async def hookah(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["hot"], reply_markup=keyboard_main.ikb_z_din)


@dp.message_handler(lambda message: "бургер-сет" in message.text.lower())
async def hookah(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["burger"], reply_markup=keyboard_main.ikb_z_burg)


@dp.message_handler(lambda message: "пицца" in message.text.lower())
async def hookah(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["pizza"], reply_markup=keyboard_main.ikb_z_pizza)


@dp.message_handler(lambda message: "отзывы" in message.text.lower())
async def tell_about_us(message: types.Message):
    await bot.send_message(message.from_user.id, "Вы можете оставить свой отзыв и получить за него подарочный кофе, а также "
                                                 "прочитать отзывы других посетителей нашего кафе",
                           reply_markup=keyboard_main.kb_tells)
    await bot.send_message(message.from_user.id, "Для возврата в главное меню нажмите кнопку", reply_markup=keyboard_main.ikb_main)


@dp.message_handler(content_types = ['photo'])
async def any_shit(message : types.Message, a="nnn"):
    await bot.send_message(5097527515, f"{message.photo[0].file_id} от {message.from_user.id}")
    #await sql_db.add_photo(message)
    #await bot.send_message(message.from_user.id, "Your photo was added to base")
    """await bot.send_message(message.from_user.id, message.from_user.id)"""


@dp.message_handler(content_types = ['video'])
async def any_shit2(message : types.Message, a="nnn"):
    await bot.send_message(message.from_user.id, message.video.file_id)


@dp.message_handler(text="корзина")
async def goto_korz(message: types.Message):
    await bot.send_message(message.from_user.id, "В данном разделе располагаются ваши заказы")




registr_admin(dp)
registr_client(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True, on_startup = on_startup)