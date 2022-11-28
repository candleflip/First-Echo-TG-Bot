from aiogram import Bot, Dispatcher, executor, types

TOKEN = "5805958193:AAGfyWDTmzTxhk-mHRC0bSDPCXcZ3yuu9BY"

bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler()
async def echo(message: types.Message):
  await message.answer(message.text)


if __name__ == '__main__':
  executor.start_polling(dispatcher, skip_updates=True)
