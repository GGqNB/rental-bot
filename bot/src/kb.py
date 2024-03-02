from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="📹Аренда техники", callback_data="rent"),
    InlineKeyboardButton(text="💬 Связаться с ренталом", callback_data="feedback_rent")],
    # [InlineKeyboardButton(text="💳 Корзина", callback_data="cart"),
    [InlineKeyboardButton(text="❔ Часто задаваемые вопросы", callback_data="faq")],
]

control_product = [
[InlineKeyboardButton(text ="Предыдущий", callback_data="prev_object:0"),
InlineKeyboardButton(text = "Следующий", callback_data="next_object:0")],
# [InlineKeyboardButton(text="👩🏻В корзину", callback_data="product_in_cart")],
[InlineKeyboardButton(text="🔙Назад в меню", callback_data="home")],
]


rent_category = [
    [InlineKeyboardButton(text="📷 Камеры", callback_data="go_product:1")],
    [InlineKeyboardButton(text="🖲️ Объективы", callback_data="go_product:2")],
    [InlineKeyboardButton(text="🗜️ Стабилизация и штативы", callback_data="stabs")],
    [InlineKeyboardButton(text="🕹️ Операторское оборудование", callback_data="operator_equip")],
    [InlineKeyboardButton(text="💡 Световое оборудование", callback_data="light_equip")],
    [InlineKeyboardButton(text="🎶 Звуковое оборудование", callback_data="sound_equip")],
    [InlineKeyboardButton(text="🎒 Аксессуары", callback_data="accessories")],
    [InlineKeyboardButton(text="🚛 Транспорт", callback_data="transport")],
    # [InlineKeyboardButton(text="Назад в меню", callback_data="home")],
]


stabs_category = [
    [InlineKeyboardButton(text="Электронные стабилизаторы", callback_data="go_product:3")],
    [InlineKeyboardButton(text="🖼 Штативы и моноподы", callback_data="go_product:4")],
    [InlineKeyboardButton(text="💳 Механическая стабилизация", callback_data="go_product:5")],
    [InlineKeyboardButton(text="🔙Назад к категориям", callback_data="rent")]
]

operator_equip_category = [
  ["Видеомониторы", "go_product:6"],
  ["🖼Сендеры", "go_product:7"],
  ["Суфлеры", "go_product:8"],
  ["Компендиумы", "go_product:9"],
  ["Фильтры", "go_product:10"],
  ["Коммутация", "go_product:11"],
  ["Камерный навес", "go_product:12"],
  ["👩🏻‍🦽Назад к категориям", "rent"]
]

light_equip_category = [
  ["LED - приборы", "go_product:13"],
  ["🖼Стойки и грип", "go_product:14"],
  ["Светоформулирующие насадки", "go_product:15"],
  ["👩🏻‍🦽Назад к категориям", "rent"]
]

sound_equip_category = [
  ["Рекордеры", "go_product:16"],
  ["🖼Петличные системы", "go_product:17"],
  ["Накамерные микрофоны", "go_product:18"],
  ["Направленные микрофоны", "go_product:19"],
  ["Комплектующие", "go_product:20"],
  ["👩🏻‍🦽Назад к категориям", "rent"]
]
accessories_category = [
  ["Карты памяти", "go_product:21"],
  ["🖼Спецэффекты", "go_product:22"],
  ["Услуги", "go_product:23"],
  ["Кабеля", "go_product:24"],
  ["Аккумуляторы", "go_product:25"],
  ["👩🏻‍🦽Назад к категориям", "rent"]
]

transport_category = [
  ["Технические машины", "go_product:26"],
  ["Машины для съемочной группы", "go_product:27"],
  ["👩🏻‍🦽Назад к категориям", "rent"]
]

kb_operator_equip = []
for category in operator_equip_category:
    kb_operator_equip.append([InlineKeyboardButton(text=category[0], callback_data=category[1])])

kb_light_equip = []
for category in light_equip_category:
    kb_light_equip.append([InlineKeyboardButton(text=category[0], callback_data=category[1])])

kb_sound_equip = []
for category in sound_equip_category:
    kb_sound_equip.append([InlineKeyboardButton(text=category[0], callback_data=category[1])])

kb_accessories = []
for category in accessories_category:
    kb_accessories.append([InlineKeyboardButton(text=category[0], callback_data=category[1])])
    

kb_transport = []
for category in transport_category:
    kb_transport.append([InlineKeyboardButton(text=category[0], callback_data=category[1])])

menu = InlineKeyboardMarkup(inline_keyboard=menu)

control_product = InlineKeyboardMarkup(inline_keyboard=control_product)

rent_category = InlineKeyboardMarkup(inline_keyboard=rent_category)
stabs_category = InlineKeyboardMarkup(inline_keyboard=stabs_category)
kb_operator_equip = InlineKeyboardMarkup(inline_keyboard=kb_operator_equip)
kb_light_equip = InlineKeyboardMarkup(inline_keyboard=kb_light_equip)
kb_sound_equip = InlineKeyboardMarkup(inline_keyboard=kb_sound_equip)
kb_accessories = InlineKeyboardMarkup(inline_keyboard=kb_accessories)
kb_transport = InlineKeyboardMarkup(inline_keyboard=kb_transport)


exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="🛒 Моя корзина")],[KeyboardButton(text="🔙 Выйти в меню")]], resize_keyboard=True)
add_cart_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Добавить в корзину ➕")],[KeyboardButton(text="🛒 Моя корзина")],[KeyboardButton(text="🔙 Выйти в меню")]], resize_keyboard=True)

gen_text = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Сделай")]], resize_keyboard=True)

iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🔙 Выйти в меню", callback_data="menu")]])

entry_cart_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="🛒 Моя корзина")],[KeyboardButton(text="Отправить на обр.связь")],[KeyboardButton(text="Очистить корзину")],[KeyboardButton(text="🔙 Выйти в меню")]], resize_keyboard=True)

