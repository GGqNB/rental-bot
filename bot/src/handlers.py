from aiogram import types, F, Router, Bot
from utils import product_text, cart_entry, cart_push
from webhook import request_product, add_cart, my_cart, clear_cart
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types.input_file import FSInputFile
import kb
import text
from aiogram import flags
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery 
from config import ADMIN_ID
from aiogram.fsm.state import StatesGroup, State
router = Router()


    
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer_photo(
        photo=text.main_photo,
        caption=text.greet.format(name=msg.from_user.full_name),
        reply_markup=kb.menu
        )
    # await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)
    

@router.message(F.text == 'Меню')
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "🔙 Выйти в меню")
async def menu(msg: Message):
     await msg.answer_photo(
        photo=text.main_photo,
        caption=text.menu,
        reply_markup=kb.menu
        )

# @router.message(F.text)
# async def give_me_id(msg: Message):
#     await msg.answer(f'Your id - {msg.from_user.id}')
    
@router.callback_query(F.data == "home")
async def back_menu(clbck: CallbackQuery):
    await clbck.message.delete()
    await clbck.message.answer(
       text=text.rent_text, 
       reply_markup=kb.menu)

@router.message(F.photo)
async def photo_hadnler(msg: Message):
    photo_data = msg.photo[-1]
    await msg.answer(f'{photo_data}')

@router.callback_query(F.data == "rent")
async def show_rent(clbck: CallbackQuery):
   await clbck.message.delete()
   await clbck.message.answer(
       text='-', 
       reply_markup=kb.exit_kb)
   
   await clbck.message.answer(
       text=text.rent_text, 
       reply_markup=kb.rent_category)
   

@router.callback_query(F.data == "stabs")
async def show_stabs(clbck: CallbackQuery):
   await clbck.message.delete()
   await clbck.message.answer(
       text=text.stabs_text, 
       reply_markup=kb.stabs_category)

@router.callback_query(F.data == "operator_equip")
async def show_operator_equip(clbck: CallbackQuery):
   await clbck.message.delete()
   await clbck.message.answer(
       text=text.operator_equip_text, 
       reply_markup=kb.kb_operator_equip)

@router.callback_query(F.data == "light_equip")
async def show_light_equip(clbck: CallbackQuery):
   await clbck.message.delete()
   await clbck.message.answer(
       text=text.light_equip_text, 
       reply_markup=kb.kb_light_equip)

@router.callback_query(F.data == "sound_equip")
async def show_sound_equip(clbck: CallbackQuery):
   await clbck.message.delete()
   await clbck.message.answer(
       text=text.sound_equip_text, 
       reply_markup=kb.kb_sound_equip)
   
@router.callback_query(F.data == "accessories")
async def show_sound_equip(clbck: CallbackQuery):
   await clbck.message.delete()
   await clbck.message.answer(
       text=text.accessories_text, 
       reply_markup=kb.kb_accessories)

@router.callback_query(F.data == "transport")
async def show_transport_equip(clbck: CallbackQuery):
   await clbck.message.delete()
   await clbck.message.answer(
       text=text.transport_text, 
       reply_markup=kb.kb_transport)

@router.callback_query(F.data == "feedback_rent")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.delete()
    await clbck.message.answer(text.feedback_rent_text, reply_markup=kb.exit_kb)



# @router.callback_query(F.data == "cart")
# async def input_text_prompt(query: types.CallbackQuery):
#     await query.message.answer("Сообщение от пользователя: Корзина")
#     # await clbck.message.delete()
#     # global my_cart
#     # await mes.answer(text.cart_text, reply_markup=kb.exit_kb)
#     # my_cart = request_my_cart(mes.from_user.id)
#     # print(my_cart)
    
    
@router.callback_query(F.data == "faq")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.delete()
    await clbck.message.answer(text.faq_text, reply_markup=kb.exit_kb)


    # await clbck.message.answer("Выберите действие:", reply_markup=kb.menu)
    
#################################### Это механизм товаров
product_id = 0
data = []
current_index = 0

@router.callback_query(lambda c: c.data.startswith('go_product:'))
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    # await clbck.message.delete()
    await clbck.message.answer(text='Ищу)', reply_markup=kb.add_cart_kb)
    request = await request_product(clbck.data.split(':')[-1])
    global data
    data = (request['data'])
    if(data):
        await display_object(clbck, 0)
    else:
        await clbck.message.answer(text='Идите в меню, я не нашел(', reply_markup=kb.exit_kb)

async def display_object(clbck: CallbackQuery, index: int):
     try: 
        await clbck.message.answer_photo(photo=data[index]['photo'], caption=product_text(data[index]), reply_markup=kb.control_product)
        global product_id
        product_id = data[index]['id']
     except:
      await clbck.message.answer(product_text(data[index]), reply_markup=kb.control_product)
      product_id = data[index]['id']

    
@router.callback_query(lambda c: c.data.startswith('next_object:'))
async def next_object_callback(clbck: CallbackQuery):
    global current_index
    current_index += 1
    if current_index >= len(data):
        current_index = 0
    await clbck.message.delete() 
    await display_object(clbck, current_index)

@router.callback_query(lambda c: c.data.startswith('prev_object:'))
async def prev_object_callback(clbck: CallbackQuery):
    global current_index
    current_index -= 1
    if current_index < 0:
        current_index = len(data) - 1
    await clbck.message.delete() 
    await display_object(clbck, current_index)
    

# @router.callback_query(F.data == "product_in_cart")
# async def product_in_cart(clbck: CallbackQuery, state: FSMContext):
#     await clbck.message.delete()
#     print( product_id)
#     await clbck.message.answer(f'{clbck.message.from_user.id} ', reply_markup=kb.exit_kb)
    
@router.message(F.text == 'Добавить в корзину ➕')
async def product_in_cart_handler(message: types.Message):
   if product_id == 0 :
       await message.answer(text.problem_add_cart)
   else: 
    try:
        print(product_id)
        print(message.from_user.id)
        await add_cart(product_id, message.from_user.id)
        await message.answer(text.text_add_cart, reply_markup=kb.add_cart_kb )
    except:
        await message.answer(text.problem_text, reply_markup=kb.add_cart_kb )

cart = []

@router.message(F.text == '🛒 Моя корзина')
async def request_my_cart(mes: types.Message):
    await mes.answer(text.cart_text, reply_markup=kb.entry_cart_kb)
    global cart
    request = await my_cart(str(mes.from_user.id))
    data = (request['data'])
    if(data):
      message = await cart_entry(data)
      print(message)
      if(message):
         await mes.answer(text= message, reply_markup=kb.entry_cart_kb)
      else:
          await mes.answer(text='ДУМАЙ', reply_markup=kb.entry_cart_kb)
    else:
        await mes.answer(text=text.problem_or_empty_cart_text, reply_markup=kb.entry_cart_kb)
    # await cart_entry(cart)

@router.message(F.text == 'Очистить корзину')
async def request_my_cart(mes: types.Message):
    request =  await clear_cart(str(mes.from_user.id))
    status = request['status']
    global cart
    if(status =='success'):
        await mes.answer(text.delete_cart, reply_markup=kb.exit_kb)
        
    else: 
        await mes.answer(text.delete_cart_error, reply_markup=kb.exit_kb)


class OrderCart(StatesGroup):
    input_for_cart = State()

@router.message(F.text == 'Отправить на обр.связь')
async def input_mes_for_cart(msg: Message, state: FSMContext):
    global cart
    request = await my_cart(str(msg.from_user.id))
    data = (request['data'])
    if(data):
        await msg.answer(text.request_user_input)
        await state.set_state(OrderCart.input_for_cart)
    else:
        await msg.answer(text=text.empty_cart_on_push, reply_markup=kb.exit_kb)
        
 
@router.message(OrderCart.input_for_cart, F.text)
async def send_cart_to_admin(msg: Message, state: FSMContext, bot: Bot):
    await state.update_data(mes_for_cart=msg.text.lower())
    user_data = await state.get_data()
    request = await my_cart(str(msg.from_user.id))
    data = (request['data'])
    message = await cart_push(data, msg.from_user.full_name, msg.from_user.username, msg.text)
    if(message):
         await bot.send_message(ADMIN_ID, message)
         request =  await clear_cart(str(msg.from_user.id))
         await msg.answer(text= 'Успех, мы отправили,корзина сброшена', reply_markup=kb.exit_kb)
    else:
          await msg.answer(text='ДУМАЙ', reply_markup=kb.exit_kb)

    await state.clear()



########################################
# def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
#     """
#     Создаёт реплай-клавиатуру с кнопками в один ряд
#     :param items: список текстов для кнопок
#     :return: объект реплай-клавиатуры
#     """
#     row = [KeyboardButton(text=item) for item in items]
#     return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
