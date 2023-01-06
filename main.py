from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN
from funcs import SQL
from markups import start, give_or_get_info

bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start'])
async def first_start(message: types.Message):
  await message.answer(
    text="Вы ученик или учитель?",
    parse_mode='html',
    reply_markup=start())


@dispatcher.callback_query_handler(lambda call: call.data == 'pupil')
async def admin_updates_database(call: types.CallbackQuery):
  await call.message.answer(
    text="Вы хотите добавить информацию о себе или узнать свои баллы по математике?",
    parse_mode='html',
    reply_markup=give_or_get_info())


@dispatcher.message_handler()
async def get_math_score(message: types.Message):
  user_id = message.text

  try:
    user_id = int(user_id)
  except Exception as e:
    print(e)
    await message.answer("Пиши цифры, ты чего")
    return True

  with SQL() as cursor:
    query = f"""SELECT math
        FROM scores
        WHERE id={user_id}"""

    user_math_score = cursor.fetchall()

  if not user_math_score:
    await message.answer("Такого пользователя нет в базе данных")
    return


if __name__ == '__main__':
  executor.start_polling(dispatcher, skip_updates=True)
