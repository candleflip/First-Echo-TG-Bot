from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler()
async def echo(message: types.Message):
  await message.answer(message.text)


if __name__ == '__main__':
  executor.start_polling(dispatcher, skip_updates=True)
