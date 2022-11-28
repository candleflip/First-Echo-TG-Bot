from aiogram import Bot, Dispatcher, executor, types

TOKEN = "вставляем_сюда_свой_токен"

bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler()
async def echo(message: types.Message):
  await message.answer(message.text)


if __name__ == '__main__':
  executor.start_polling(dispatcher, skip_updates=True)
