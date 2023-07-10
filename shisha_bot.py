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
#import zakazaka

async def on_startup(_):
    print("Папа в здании")
    sql_db.db_start()


temp_user = {}
temp_mast = {}


@dp.callback_query_handler(text="в начало")
@dp.message_handler(lambda message: message.text.lower() in ["в начало", '/main'])
async def salam(message: types.Message):
    if message.from_user.id in pers.amdins:
        await bot.send_message(message.from_user.id, "Салам, родной",
                               reply_markup=keyboard_main.kb_mainwindow_admin)
    else:
        await bot.send_message(message.from_user.id, "Выберите категорию",
                               reply_markup=keyboard_main.kb_mainwindow)

@dp.message_handler(lambda message: "start" in message.text.lower())
async def start(message: types.Message):
    if message.from_user.id in pers.amdins:
        await bot.send_message(message.from_user.id, "Салам, родной",
                               reply_markup=keyboard_main.kb_mainwindow_admin)
    else:
        await bot.send_photo(message.from_user.id, photos.logo)
        await bot.send_message(message.from_user.id, "Здравствуйте, дорогой друг!\nВыберитe категорию, нажав на "
                                                     "соответствующую кнопку",
                               reply_markup=keyboard_main.kb_mainwindow)
        await sql_db.user_add(message)

@dp.message_handler(lambda message: "контакты" in message.text.lower())
async def kontakts(message: types.Message):
    await bot.send_message(message.from_user.id, "Телефон нашего launge бара - +73822570880",
                           reply_markup=keyboard_main.ikb_main)

@dp.message_handler(lambda message: "адрес" in message.text.lower())
async def adress(message: types.Message):
    await bot.send_message(message.from_user.id, "Наш launge бар расположен по адресу: г. Томск, "
                                                 "ул. Розы Люксембург, д. 72", reply_markup=keyboard_main.ikb_main)

@dp.message_handler(lambda message: "режим работы" in message.text.lower())
async def time(message: types.Message):
    await bot.send_message(message.from_user.id, "Наш launge бар открыт для гостей ежедневно с 12.00 до 03.00",
                           reply_markup=keyboard_main.ikb_main)

@dp.callback_query_handler(text="О нашем launge баре")
@dp.message_handler(lambda message: "о нашем launge баре" in message.text.lower())
async def about(message: types.Message):
    await bot.send_message(message.from_user.id, "В данном разделе Вы можете ознакомиться с "
                                                 "интерьером зала, узнать наш адрес, время работы, телефон для связи.", reply_markup=keyboard_main.kb_ourbar)
    await bot.send_message(message.from_user.id,
                           text="Выберите категорию", reply_markup=keyboard_main.ikb_main)



@dp.message_handler(lambda message: "магазин" in message.text.lower())
async def store(message: types.Message):
    await bot.send_message(message.from_user.id, "Раздел находится в разработке")


@dp.message_handler(lambda message: "аренда кальяна" in message.text.lower())
async def store(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.rent, reply_markup=keyboard_main.ikb_main)

@dp.message_handler(lambda message: "интерьер" in message.text.lower())
async def interier(message: types.Message):
    temp_user[message.from_user.id] = temp_user.get(message.from_user.id, 0)
    photo_number: int = temp_user[message.from_user.id]
    await bot.send_photo(message.from_user.id, photos.rooms[photo_number], reply_markup=keyboard_main.ikb_about)
    temp_user[message.from_user.id] = (temp_user.get(message.from_user.id, 0) + 1) % 9


@dp.callback_query_handler(text="next_photo")
async def interier2(cb: types.CallbackQuery):
    temp_user[cb.from_user.id] = temp_user.get(cb.from_user.id, 0)
    photo_number: int = temp_user[cb.from_user.id]
    photo_file = InputMediaPhoto(photos.rooms[photo_number])
    await bot.edit_message_media(media=photo_file, message_id=cb.message.message_id,
                                 chat_id=cb.message.chat.id, reply_markup=keyboard_main.ikb_about)
    temp_user[cb.from_user.id] = (temp_user.get(cb.from_user.id, 0) + 1) % 9



@dp.message_handler(lambda message: "наши мастера" in message.text.lower())
async def masters(message: types.Message):
    temp_mast[message.from_user.id] = temp_mast.get(message.from_user.id, 0)
    photo_number: int = temp_mast[message.from_user.id]
    await bot.send_photo(message.from_user.id, photos.masters_photo[photo_number],
                         reply_markup=keyboard_main.ikb_next_master)
    temp_mast[message.from_user.id] = (temp_mast.get(message.from_user.id, 0) + 1) % 4

@dp.callback_query_handler(text="next_master")
async def masters2(cb: types.CallbackQuery):
    temp_mast[cb.from_user.id] = temp_mast.get(cb.from_user.id, 0)
    photo_number: int = temp_mast[cb.from_user.id]
    photo_file = InputMediaPhoto(photos.masters_photo[photo_number])
    await bot.edit_message_media(media=photo_file, message_id=cb.message.message_id,
                                 chat_id=cb.message.chat.id, reply_markup=keyboard_main.ikb_next_master)
    temp_mast[cb.from_user.id] = (temp_mast.get(cb.from_user.id, 0) + 1) % 4


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

@dp.message_handler(lambda message: "акции" in message.text.lower())
async def actions(message: types.Message):
    await bot.send_message(message.from_user.id, "Актуальные акции в нашем lounge баре")
    for i in photos.actions:
        await bot.send_photo(message.from_user.id, i, reply_markup=keyboard_main.ikb_main)

@dp.callback_query_handler(lambda c: "menu" in c.data)
@dp.message_handler(lambda message: "меню" in message.text.lower())
async def manu(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["menu"])
    await bot.send_message(message.from_user.id, "Выберите категорию", reply_markup=keyboard_main.kb_menu)


@dp.message_handler(lambda message: "пицца" in message.text.lower())
async def pizza(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["pizza"], reply_markup=keyboard_main.ikb_main)


@dp.message_handler(lambda message: "напитки" in message.text.lower())
async def drink(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["drink"], reply_markup=keyboard_main.ikb_main)


@dp.message_handler(lambda message: "крафтовое пиво" in message.text.lower())
async def krbeer(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["krbeer"], reply_markup=keyboard_main.ikb_main)


@dp.message_handler(lambda message: "пиво" in message.text.lower())
async def beer(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["beer"], reply_markup=keyboard_main.ikb_main)


@dp.message_handler(lambda message: "чаи" in message.text.lower())
async def tea(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["tea"], reply_markup=keyboard_main.ikb_main)


@dp.message_handler(lambda message: "десерты" in message.text.lower())
async def des(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["des"], reply_markup=keyboard_main.ikb_main)


@dp.message_handler(lambda message: "снеки" in message.text.lower())
async def snack(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["snack"], reply_markup=keyboard_main.ikb_main)

@dp.message_handler(lambda message: "горячие закуски" in message.text.lower())
async def zakus(message: types.Message):
    await bot.send_photo(message.from_user.id, photos.menu["zakus"], reply_markup=keyboard_main.ikb_main)


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