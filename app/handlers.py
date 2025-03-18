from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import app.keyboards as kb
from app.database.requests import set_user
from aiogram.types import InputMediaPhoto

router = Router()
hello_img = "https://cloud.mail.ru/public/6K7Z/gwcowrfZc"
category_img = ''
contacts_img = ''
ADMIN_ID = '1184649629'


@router.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer_photo(
        photo=hello_img,
        caption='Добро пожаловать в магазин вязанных игрушек!',
        reply_markup=kb.menu)


@router.callback_query(F.data == 'contacts')
async def callback_contacts(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_media(media=InputMediaPhoto(
        media=hello_img,
        caption='''Вязание это просто!

Меня зовут Светлана, будем знакомы🤝
Создаю милые вязаные вещи. Обучаю вязанию крючком.

По вопросам и предложениям пишите: @sonasonVL'''
    ),
        reply_markup=kb.menu
    )


@router.callback_query(F.data == 'start')
async def callback_start(callback: CallbackQuery):
    await callback.answer('Вы вернулись на главное меню')
    await callback.message.edit_media(media=InputMediaPhoto(
        media=hello_img,
        caption='Добро пожаловать в магазин вязанных игрушек!'
    ),
        reply_markup=kb.menu)


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_media(media=InputMediaPhoto(
        media=hello_img,
        caption='Выберите категорию товара'
    ),
        reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]

    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=hello_img,
            caption="Выберите товар по категории"
        ),
        reply_markup=await kb.items(category_id)
    )
    await callback.answer('')


@router.callback_query(F.data.startswith('item_'))
async def item_handler(callback: CallbackQuery):
    item_id = callback.data.split('_')[1]
    item = await kb.get_item(item_id)
    await callback.message.edit_media(media=InputMediaPhoto(
        media=item.image_url,
        caption=f'{item.name}\n{item.description}\n\nЦена: {item.price} руб.',
    ),
        reply_markup=await kb.item_menu(item.category, item.id)
    )
    await callback.answer('')


@router.callback_query(F.data.startswith('order_item_'))
async def set_order(callback: CallbackQuery):
    item_id = callback.data.split('_')[2]
    item = await kb.get_item(item_id)
    await callback.message.edit_media(media=InputMediaPhoto(
        media=item.image_url,
        caption=f'Вы хотите заказать:\n{item.name}\n{item.description}\n\nЦена: {item.price} руб.',
    )

    )

    await callback.answer('')
