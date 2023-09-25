from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from Keyboard import  get_keyboard
from config import TOKEN_API
from database import add_tasks, clear_tasks, load_tasks
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=storage)


class Tasks(StatesGroup):  #состояния FSM

    wait = State()


async def load_task(user_id):
    tasks = await load_tasks(user_id)

    if (len(tasks) > 0):
        count = 0
        text = 'Список задач: \n\n'
        for task in tasks:
            count += 1
            text += f'{count}. {task[1]}\n'
        return text
    else:
        return 'Список задач пуст'          #функция вывода списка задач


@dp.message_handler(commands=['start'])    #обработчик команды "start"
async def cmd_start(message: types.Message):
    await message.answer(await load_task(message.chat.id), reply_markup=get_keyboard())


@dp.callback_query_handler(state='*')     #обработка inline keyboard
async def callback_kb_add(callback: types.CallbackQuery):
    if callback.data == 'kb_add':         #обработка callback'a
        await callback.message.answer('Введите название задачи')
        await Tasks.wait.set()            #изменение состояния FSM
    elif callback.data == 'kb_clear':
        await clear_tasks(callback.message.chat.id)   #очистка БД
        await callback.message.answer(await load_task(callback.message.chat.id), reply_markup=get_keyboard())


@dp.message_handler(state=Tasks.wait)
async def add_task(message: types.Message, state: FSMContext):
    await add_tasks(message.text, message.chat.id)  #добавление сообщения в БД
    await state.finish()  #финальное состояния FSM
    await message.answer(await load_task(message.chat.id), reply_markup=get_keyboard())