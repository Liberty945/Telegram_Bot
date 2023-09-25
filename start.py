from handlers import *
from aiogram import executor
from SUandSD import on_shutdown, db_startup

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=db_startup,
                           on_shutdown=on_shutdown,
                           )                            #запуск Бота