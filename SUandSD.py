from database import db_start

async def on_shutdown(_):
    print ('Бот остановлен')    #функция выключения Бота

async def db_startup(_):
    await db_start()            #функция создания БД