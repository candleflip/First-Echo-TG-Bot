from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start():
  markup = InlineKeyboardMarkup(row_width=1)
  markup.add(InlineKeyboardButton('Ученик', callback_data='pupil'),
             InlineKeyboardButton('Учитель', callback_data='teacher'))

  return markup


def give_or_get_info():
  markup = InlineKeyboardMarkup(row_width=1)
  markup.add(InlineKeyboardButton('Добавить', callback_data='give'),
             InlineKeyboardButton('Узнать', callback_data='get'))

  return markup

