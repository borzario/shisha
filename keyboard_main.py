from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

ib_main = InlineKeyboardButton(text="В начало", callback_data="в начало")

b_time = KeyboardButton("Режим работы")
b_adress = KeyboardButton("Адрес")
b_contacts = KeyboardButton("Контакты")
b_first = KeyboardButton("В начало")
b_usligi = KeyboardButton("Услуги нашего заведения")
b_about = KeyboardButton("О нашем launge баре")
b_korzina = KeyboardButton("Корзина")
b_store = KeyboardButton("Магазин")
kb_mainwindow = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mainwindow.row(b_usligi).row(b_about).row(b_store)


b_masters = KeyboardButton("Наши мастера")
b_interier = KeyboardButton("Интерьер")
b_tells = KeyboardButton("Отзывы")
ib_about = InlineKeyboardButton(text="Назад", callback_data="О нашем launge баре")
ib_next_photo = InlineKeyboardButton(text="Следующее фото", callback_data="next_photo")
ib_next_master = InlineKeyboardButton(text="Следующий", callback_data="next_master")
ib_next_tell = InlineKeyboardButton(text="Cлучайный отзыв", callback_data="next_tell")
kb_ourbar = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ourbar.row(b_interier).row(b_time, b_adress, b_contacts).row(b_masters).row(b_tells)
ikb_main = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).row(ib_main)
ikb_about = InlineKeyboardMarkup(row_width=1).row(ib_main, ib_next_photo)
ikb_tells = InlineKeyboardMarkup(row_width=1).row(ib_main, ib_next_tell)
ikb_next_master = InlineKeyboardMarkup(row_width=1).row(ib_main, ib_next_master)

b_hooka = KeyboardButton("Кальянные радости")
b_menu = KeyboardButton("Меню")
b_stol = KeyboardButton("Забронировать стол")
b_actions = KeyboardButton("Акции")
b_rent_h = KeyboardButton("Аренда кальяна")
kb_uslugi = ReplyKeyboardMarkup(resize_keyboard=True)
kb_uslugi.row(b_menu).row(b_hooka,).row(b_actions).row(b_rent_h).row(b_stol)

b_pizza = KeyboardButton("Пицца")
b_drink = KeyboardButton("Напитки")
b_krbeer = KeyboardButton("Крафтовое пиво")
b_beer = KeyboardButton("Пиво")
b_tea = KeyboardButton("Чаи")
b_des = KeyboardButton("Десерты")
b_snack = KeyboardButton("Снеки")
b_eda = KeyboardButton("Горячие закуски")
kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.row(b_pizza, b_snack, b_des).row(b_eda).row(b_krbeer, b_beer).row(b_tea, b_drink)


ib_uslugi = InlineKeyboardButton(text="Назад", callback_data="Услуги нашего заведения")
b_tea = KeyboardButton("Чаи")
b_cold = KeyboardButton("Прохладительные напитки")

kb_bar = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bar.row(b_tea).row(b_cold).row(b_stol)
ikb_uslugi = InlineKeyboardMarkup(row_width=1).row(ib_uslugi, ib_main)

b_tell_about = KeyboardButton("Оставить отзыв")
b_read_about = KeyboardButton("Ознакомиться с отзывами")
kb_tells = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tells.row(b_tell_about).row(b_read_about)


b_nasmene = KeyboardButton("Я на смене")
b_bron_accapt = KeyboardButton("Подтвердить бронь")
b_tell_accapt = KeyboardButton("Разрешить отзыв")
b_bron_no = KeyboardButton("отменить бронь")
b_spam = KeyboardButton("Запилить рассылку")
kb_mainwindow_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mainwindow_admin.row(b_nasmene).row(b_bron_accapt, b_bron_no).row(b_spam)


b_cancel = KeyboardButton("Отмена")
ib_cancel = InlineKeyboardButton(text="Отмена", callback_data="cancel")
ikb_cancel = InlineKeyboardMarkup(row_width=1).row(ib_cancel)

kb_zakaz = ReplyKeyboardMarkup(resize_keyboard=True)
kb_zakaz.row(b_cancel).row(b_usligi)

b_who_at_work = KeyboardButton("Кто на смене?")
kb_who_at_work = ReplyKeyboardMarkup(resize_keyboard=True).row(b_who_at_work).row(b_first)


"""Buttons for zakazaka"""

ib_korz = InlineKeyboardButton(text="Корзина", callback_data="корзина")
ib_menu = InlineKeyboardButton(text="Меню", callback_data="меню")

""" пицца _________________________________________________________________________________________________"""
ib_zakaz_pizza = InlineKeyboardButton(text="Заказать", callback_data="z_pizza")
ikb_z_pizza = InlineKeyboardMarkup(row_width=1).row(ib_main, ib_zakaz_pizza)

ib_cheeze_25 = InlineKeyboardButton(text="Сырная с пряной грушей (25см)", callback_data="zakp клоун25")
ib_cheeze_35 = InlineKeyboardButton(text="35 см", callback_data="zakp клоун35")
ib_cheeze_45 = InlineKeyboardButton(text="45 см", callback_data="zakp клоун45")

ib_pep_25 = InlineKeyboardButton(text="Пеперони (25см)", callback_data="zakp пеп25")
ib_pep_35 = InlineKeyboardButton(text="35 см", callback_data="zakp пеп35")
ib_pep_45 = InlineKeyboardButton(text="45 см", callback_data="zakp пеп45")

ib_mor_25 = InlineKeyboardButton(text="Морская (25см)", callback_data="zakp мор25")
ib_mor_35 = InlineKeyboardButton(text="35 см", callback_data="zakp мор35")
ib_mor_45 = InlineKeyboardButton(text="45 см", callback_data="zakp мор45")

ib_meat_25 = InlineKeyboardButton(text="Мясная (25см)", callback_data="zakp мяс25")
ib_meat_35 = InlineKeyboardButton(text="35 см", callback_data="zakp мяс35")
ib_meat_45 = InlineKeyboardButton(text="45 см", callback_data="zakp мяс45")

ikb_types_of_pizza = InlineKeyboardMarkup(row_width=1).row(ib_cheeze_25).row(ib_cheeze_35, ib_cheeze_45).\
    row(ib_pep_25).row(ib_pep_35, ib_pep_45).row(ib_mor_25).row(ib_mor_35, ib_mor_45).row(ib_meat_25).\
    row(ib_meat_35, ib_meat_45).row(ib_menu, ib_korz)

""" бургеры _________________________________________________________________________________________________"""
ib_zakaz_burg = InlineKeyboardButton(text="Заказать", callback_data="z_burg")
ikb_z_burg = InlineKeyboardMarkup(row_width=1).row(ib_main, ib_zakaz_burg)

ib_chik = InlineKeyboardButton(text="Чикен бургер, картошка фри, соус", callback_data="zakp чик")
ib_chik2 = InlineKeyboardButton(text="Дабл чикен бургер, картошка фри, соус", callback_data="zakp чик2")

ib_bif = InlineKeyboardButton(text="Биф бургер, картофель по деревенски, соус", callback_data="zakp биф")
ib_fish = InlineKeyboardButton(text="Fish бургер, картофельные чурос, соус", callback_data="zakp чур")
ib_ket = InlineKeyboardButton(text="Кетчуп", callback_data="zakp кетч")

ib_sir = InlineKeyboardButton(text="Сырный соус", callback_data="zakp сырный")
ib_maz = InlineKeyboardButton(text="Майонез", callback_data="zakp мазик")
ib_tar = InlineKeyboardButton(text="Тар-Тар", callback_data="zakp тар")

ikb_types_of_burg = InlineKeyboardMarkup(row_width=1).row(ib_chik).row(ib_chik2).\
    row(ib_bif).row(ib_fish).row(ib_ket, ib_tar).row(ib_maz, ib_sir).row(ib_menu, ib_korz)


ib_clear_gods = InlineKeyboardButton(text="Очистить корзину", callback_data="clear all")
ib_pay_gods = InlineKeyboardButton(text="Оплатить заказ", callback_data=f"pay")
ikb_clear_pay = InlineKeyboardMarkup(row_width=1).row(ib_clear_gods, ib_pay_gods)

""" закуски _________________________________________________________________________________________________"""
ib_zakaz_zakus = InlineKeyboardButton(text="Заказать", callback_data="z_zakus")
ikb_z_zakus = InlineKeyboardMarkup(row_width=1).row(ib_main, ib_zakaz_zakus)

ib_kfl = InlineKeyboardButton(text="Картошка фри стандарт", callback_data="zakp кфм")
ib_kfb = InlineKeyboardButton(text="Картошка фри большая порция", callback_data="zakp кфб")

ib_lukl = InlineKeyboardButton(text="Луковые кольца стандарт", callback_data="zakp лукм")
ib_lukb= InlineKeyboardButton(text="Луковые кольца большая порция", callback_data="zakp лукб")

ib_nagl = InlineKeyboardButton(text="Наггетсы стандарт", callback_data="zakp нагм")
ib_nagb = InlineKeyboardButton(text="Наггетсы большая порция", callback_data="zakp нагб")

ib_sirpl = InlineKeyboardButton(text="Сырные палочки стандарт", callback_data="zakp сырм")
ib_sirpb = InlineKeyboardButton(text="Сырные палочки большая порция", callback_data="zakp сырб")

ib_krabl = InlineKeyboardButton(text="Клешни краба стандарт", callback_data="zakp клкрм")
ib_krabb= InlineKeyboardButton(text="Клешни краба большая порция", callback_data="zakp клкрм")

ib_mix_zak = InlineKeyboardButton(text="Микс закусок", callback_data="zakp миксз")

ikb_types_of_zak = InlineKeyboardMarkup(row_width=1).row(ib_kfl, ib_kfb).row(ib_lukl, ib_lukb).row(ib_nagl, ib_nagb).\
    row(ib_sirpl, ib_sirpb).row(ib_krabl, ib_krabb).row(ib_mix_zak).row(ib_menu, ib_korz)
""" ___________________________________________________________________________________________________________"""

""" салаты _________________________________________________________________________________________________"""
ib_zakaz_salat = InlineKeyboardButton(text="Заказать", callback_data="z_salat")
ikb_z_salat = InlineKeyboardMarkup(row_width=1).row(ib_main, ib_zakaz_salat)

ib_grech = InlineKeyboardButton(text="Гречский", callback_data="zakp греч")
ib_cezkur= InlineKeyboardButton(text="Цезарь с курицей", callback_data="zakp цезкур")

ib_cazkr = InlineKeyboardButton(text="Цезарь с криветкой", callback_data="zakp цезкр")
ib_veget= InlineKeyboardButton(text="Овощная нарезка", callback_data="zakp овощн")

ib_solen = InlineKeyboardButton(text="Соления", callback_data="zakp солен")
ib_fruct = InlineKeyboardButton(text="Фруктовая нарезка", callback_data="zakp фрукт")

ib_sirplate = InlineKeyboardButton(text="Сырная тарелка", callback_data="zakp сыртар")
ib_meatplate = InlineKeyboardButton(text="Мясная тарелка", callback_data="zakp мястар")


ikb_types_of_salat = InlineKeyboardMarkup(row_width=1).row(ib_grech).row(ib_cezkur).row(ib_cazkr).\
    row(ib_veget).row(ib_solen).row(ib_fruct).row(ib_sirplate).row(ib_meatplate).row(ib_menu, ib_korz)
""" ___________________________________________________________________________________________________________"""

""" напитки _________________________________________________________________________________________________"""
ib_zakaz_drink = InlineKeyboardButton(text="Заказать", callback_data="z_drink")
ikb_z_drink = InlineKeyboardMarkup(row_width=1).row(ib_main, ib_zakaz_drink)

ib_espresso = InlineKeyboardButton(text="Эспрессо", callback_data="zakp эспр")
ib_espresso_milk = InlineKeyboardButton(text="Эспрессо с молоком", callback_data="zakp эспм")

ib_amerikano = InlineKeyboardButton(text="Американо", callback_data="zakp америк")
ib_amerikano_milk = InlineKeyboardButton(text="Американо с молоком", callback_data="zakp америкм")

ib_kapuch = InlineKeyboardButton(text="Капучино", callback_data="zakp капуч")

ib_latte = InlineKeyboardButton(text="Латте", callback_data="zakp латте")
ib_flat = InlineKeyboardButton(text="Флэт уайт", callback_data="zakp флэт")

ib_tea = InlineKeyboardButton(text="Чай", callback_data="zakp чай")
ib_kokao = InlineKeyboardButton(text="Какао", callback_data="zakp какао")

ib_lim_l = InlineKeyboardButton(text="Лимонад 0.3 л", callback_data="zakp лимм")
ib_lim_b = InlineKeyboardButton(text="Лимонад 0.5 л", callback_data="zakp лимб")

ib_moh_l = InlineKeyboardButton(text="Мохито 0.3 л", callback_data="zakp мохм")
ib_moh_b = InlineKeyboardButton(text="Мохито 0.5 л", callback_data="zakp мохб")

ib_kvas_l= InlineKeyboardButton(text="Квас 0.3 л", callback_data="zakp квасм")
ib_kvas_b = InlineKeyboardButton(text="Квас 0.5 л", callback_data="zakp квасб")

ib_fanta = InlineKeyboardButton(text="Фанта", callback_data="zakp фант")
ib_kola = InlineKeyboardButton(text="Кола", callback_data="zakp кола")
ib_sprite = InlineKeyboardButton(text="Спрайт", callback_data="zakp спрайт")

ib_sok_l = InlineKeyboardButton(text="Сок 0.2 л", callback_data="zakp сокм")
ib_sok_b = InlineKeyboardButton(text="Сок 1 л", callback_data="zakp сокб")

ikb_types_of_drink = InlineKeyboardMarkup(row_width=1).row(ib_espresso, ib_espresso_milk).row(ib_amerikano, ib_amerikano_milk)\
    .row(ib_kapuch).row(ib_latte, ib_flat).row(ib_tea, ib_kokao).row(ib_lim_l, ib_lim_b).row(ib_moh_l, ib_moh_b)\
    .row(ib_kvas_l, ib_kvas_b).row(ib_fanta, ib_kola, ib_sprite).row(ib_menu, ib_korz)
""" ___________________________________________________________________________________________________________"""

""" завтраки _________________________________________________________________________________________________"""
ib_zakaz_brekf = InlineKeyboardButton(text="Заказать", callback_data="z_brekf")
ikb_z_brekf = InlineKeyboardMarkup(row_width=1).row(ib_main, ib_zakaz_brekf)

ib_sirn_yag = InlineKeyboardButton(text="Сырники с ягодами", callback_data="zakp сырняг")
ib_sirn_sol = InlineKeyboardButton(text="Сырники с лососем", callback_data="zakp сырнсол")

ib_varen = InlineKeyboardButton(text="Вареники", callback_data="zakp вареник")
ib_pular = InlineKeyboardButton(text="Омлет Пуляр", callback_data="zakp амлпул")

ib_omlet = InlineKeyboardButton(text="Омлет", callback_data="zakp амло")
ib_glaz = InlineKeyboardButton(text="Глазунья", callback_data="zakp глазун")

ib_shaksh = InlineKeyboardButton(text="Шакшука", callback_data="zakp шакшука")
ib_skrambl = InlineKeyboardButton(text="Скрэмбл", callback_data="zakp скрэмбл")

ib_vaf_los = InlineKeyboardButton(text="Вафля с лососем", callback_data="zakp вафлос")
ib_vaf_ug = InlineKeyboardButton(text="Вафля с угрем", callback_data="zakp вафугр")

ib_vaf_kur = InlineKeyboardButton(text="Вафля с грудкой", callback_data="zakp вафгр")
ib_kash_yag = InlineKeyboardButton(text="Овсянка с ягодами", callback_data="zakp овсяг")

ib_kash_kur = InlineKeyboardButton(text="Овсянка с курицей", callback_data="zakp овскур")
ib_ekspr_set = InlineKeyboardButton(text="Экспресс-сет", callback_data="zakp экспрсет")
ib_fit_set = InlineKeyboardButton(text="Фитнес-сет", callback_data="zakp фитсет")

ikb_types_of_brekf = InlineKeyboardMarkup(row_width=1).row(ib_sirn_yag, ib_sirn_sol).row(ib_varen)\
    .row(ib_pular, ib_omlet).row(ib_glaz, ib_shaksh, ib_skrambl).row(ib_vaf_kur).row(ib_vaf_los, ib_vaf_ug)\
    .row(ib_kash_kur, ib_kash_yag).row(ib_ekspr_set, ib_fit_set).row(ib_menu, ib_korz)
""" ___________________________________________________________________________________________________________"""

""" горячее _________________________________________________________________________________________________"""
ib_zakaz_din = InlineKeyboardButton(text="Заказать", callback_data="z_din")
ikb_z_din = InlineKeyboardMarkup(row_width=1).row(ib_main, ib_zakaz_din)

ib_kur_sup = InlineKeyboardButton(text="Куриный суп", callback_data="zakp курсуп")
ib_steik_sv = InlineKeyboardButton(text="Стейк из свинины", callback_data="zakp стксв")

ib_grudka = InlineKeyboardButton(text="Куриная грудка", callback_data="zakp кургр")
ib_midii = InlineKeyboardButton(text="Мидии", callback_data="zakp мидии")

ib_osteik_rib = InlineKeyboardButton(text="Стейк Рибай", callback_data="zakp сткриб")
ib_pasta = InlineKeyboardButton(text="Паста Карбонара", callback_data="zakp паст")

ib_losos = InlineKeyboardButton(text="Лосось", callback_data="zakp лосось")

ikb_types_of_din = InlineKeyboardMarkup(row_width=1).row(ib_kur_sup).row(ib_steik_sv)\
    .row(ib_grudka).row(ib_midii).row(ib_osteik_rib).row(ib_pasta)\
    .row(ib_losos).row(ib_menu, ib_korz)
""" ___________________________________________________________________________________________________________"""