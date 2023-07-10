from aiogram import types
from aiogram.types import ContentType

import data_base.goods
import keyboard_main
import pers
import tok
from create_bot import dp, bot
from data_base import sql_db


@dp.callback_query_handler(text="z_pizza")
async def z_pizza(cb: types.CallbackQuery):
    await bot.send_message(cb.from_user.id, text="Выберите пиццу", reply_markup=keyboard_main.ikb_types_of_pizza)


@dp.callback_query_handler(text="z_burg")
async def z_burg(cb: types.CallbackQuery):
    await bot.send_message(cb.from_user.id, text="Выберите бургер сет", reply_markup=keyboard_main.ikb_types_of_burg)


@dp.callback_query_handler(text="z_zakus")
async def z_zakus(cb: types.CallbackQuery):
    await bot.send_message(cb.from_user.id, text="Выберите закуску", reply_markup=keyboard_main.ikb_types_of_zak)


@dp.callback_query_handler(text="z_drink")
async def z_drink(cb: types.CallbackQuery):
    await bot.send_message(cb.from_user.id, text="Выберите напиток", reply_markup=keyboard_main.ikb_types_of_drink)


@dp.callback_query_handler(text="z_brekf")
async def z_drink(cb: types.CallbackQuery):
    await bot.send_message(cb.from_user.id, text="Выберите завтрак", reply_markup=keyboard_main.ikb_types_of_brekf)


@dp.callback_query_handler(text="z_salat")
async def z_salat(cb: types.CallbackQuery):
    await bot.send_message(cb.from_user.id, text="Выберите салат", reply_markup=keyboard_main.ikb_types_of_salat)


@dp.callback_query_handler(text="z_din")
async def z_din(cb: types.CallbackQuery):
    await bot.send_message(cb.from_user.id, text="Выберите горячее", reply_markup=keyboard_main.ikb_types_of_din)


@dp.callback_query_handler(lambda c: c.data[:5] == "zakp ")
async def z_pizza_zak(cb: types.CallbackQuery):
    await sql_db.add_zak(cb.from_user.id, cb.data[5:])
    await bot.answer_callback_query(cb.id, text=f"Товар\n{data_base.goods.gods[cb.data[5:]][0]} \nдобавлен в корзину",
                                    show_alert=True)


@dp.callback_query_handler(lambda c: "корзина" in c.data)
@dp.message_handler(lambda message: "корзина" in message.text.lower())
async def look_korzina(message: types.Message):
    korz: list = await sql_db.get_tov_from_korzina(message.from_user.id)
    gods_list = ''
    gods_cost = 0
    for n, i in enumerate(korz, start=1):
        gods_list += f"{n} - {i[2]}, {i[3]} рублей\n"
        gods_cost += i[3]
    await bot.send_message(message.from_user.id, f"Ваш заказ:\n{gods_list}Стоимость заказа: {gods_cost} рублей",
                           reply_markup=keyboard_main.ikb_clear_pay)


@dp.callback_query_handler(lambda c: "clear all" in c.data)
async def clear_korz(cb: types.CallbackQuery):
    await sql_db.clear_korzinu(cb.from_user.id)
    korz: list = await sql_db.get_tov_from_korzina(cb.from_user.id)
    gods_list = ''
    gods_cost = 0
    for i in korz:
        gods_list += f"{i[0]} - {i[2]}, {i[3]} рублей\n"
        gods_cost += i[3]
    await bot.edit_message_text(message_id=cb.message.message_id, chat_id=cb.message.chat.id,
                                text=f"Ваш заказ:\n{gods_list}Стоимость заказа: {gods_cost} рублей",
                                reply_markup=keyboard_main.ikb_clear_pay)


@dp.callback_query_handler(lambda c: c.data == "pay")
async def pay_for_gods(cb: types.CallbackQuery):
    korz: list = await sql_db.get_tov_from_korzina(cb.from_user.id)
    gods_cost = 0
    for i in korz:
        gods_cost += i[3]
    PRICE = types.LabeledPrice(label='Платеж за выбранные товары', amount=gods_cost * 100)
    await bot.send_invoice(
        cb.from_user.id,
        title="Платеж по заказу в ТОкафе",
        description="набор еды",
        provider_token=tok.PTOKEN,
        currency='rub',
        photo_url="https://downloader.disk.yandex.ru/preview/5845f064cca6fabfa96a25724af14a90fc4f714088f313b319c36fc8"
                  "212caca8/6492c5d0/McV6VIm9D7msjbC8Hvkeb31cjrxiZo7ZKy3V8T-r2ZGzlbinlf9qp9Dp0DtGpWmsRbUhgAjfGUFefBMN"
                  "62q59A%3D%3D?uid=0&filename=IMG_9094.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpe"
                  "g&owner_uid=0&tknv=v2&size=2048x2048",
        photo_height=471,
        photo_width=600,
        # photo_size=61100,
        is_flexible=False,
        prices=[PRICE],
        start_parameter='to_cafe_example',
        payload='some-invoice-payload-for-our-internal-use')


@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    korz: list = await sql_db.get_tov_from_korzina(message.from_user.id)
    gods_list = ''
    gods_cost = 0
    for i in korz:
        gods_list += f"{i[0]} - {i[2]}, {i[3]} рублей\n"
        gods_cost += i[3]
    for i in pers.amdins:
        await bot.send_message(i, text=f"Родная, новый заказ:\n{gods_list}Стоимость заказа: {gods_cost} рублей")
    await sql_db.clear_korzinu(message.from_user.id)
    await bot.send_message(message.from_user.id, "Платеж прошел успешно")
