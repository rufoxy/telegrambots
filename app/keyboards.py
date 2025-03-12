from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database.requests import get_categories, get_items_by_categories

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])


async def categories():
    all_categories = get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.row(InlineKeyboardButton(text=category.name,
                     callback_date=f'category_{category.id}'))
    keyboard.row(InlineKeyboardButton(
        text='На главную', callback_data='start'))
    return keyboard.as_markup()


async def items():
    all_items = get_items_by_categories(category_id)
    keyboard = InlineKeyboardBuilder
    for item in all_items:
        keyboard.row(InlineKeyboardButton(
            text=item.name, callback_date=f'item_{item.id}'))
    keyboard.row(InlineKeyboardButton(
        text='К категориям', callback_date='catalog'))
    return keyboard.as_markup()


async def back_to_category():
    InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
        text='Назад', callback_data=f'category_{category_id}'),]])
