import sqlite3 as sq

async def db_start():
    global db, cur

    db = sq.connect('tbdatabase.db')
    cur = db.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
    user_id TEXT,
    task TEXT)
    ''')
                        #функция создания БД
    db.commit()


async def add_tasks(task, user_id):
    cur.execute("INSERT INTO tasks VALUES(?, ?)", (user_id,task,))
    db.commit()  #функция добавления информации в БД

async def load_tasks(user_id):
    tasks = cur.execute('SELECT * FROM tasks WHERE user_id = ?', (user_id,)).fetchall()
    db.commit()
    return tasks   #функция вывода информации из БД

async def clear_tasks(user_id):
    qwerty = "delete from tasks where user_id = (?)"
    cur.execute(qwerty, (user_id,))
    db.commit()     #функция очистки БД